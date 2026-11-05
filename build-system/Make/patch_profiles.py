import datetime, os, sys, plistlib, subprocess, tempfile, re

ORIG = 'ph.telegra.Telegraph'
NEW  = 'com.hundredgram'
DIR  = 'build-system/fake-codesigning/profiles'

result = subprocess.run(['security', 'find-identity', '-p', 'codesigning', 'temp.keychain'],
                        capture_output=True, text=True)
m = re.search(r'\) [0-9A-F]+ "(.*?)"', result.stdout)
if not m:
    print('ERROR: no signing identity found in temp.keychain')
    print(result.stdout)
    sys.exit(1)
identity = m.group(1)
print(f'Signing identity: {identity}')

for fname in sorted(os.listdir(DIR)):
    if not fname.endswith('.mobileprovision'):
        continue
    fpath = os.path.join(DIR, fname)
    dec = subprocess.run(['security', 'cms', '-D', '-i', fpath], capture_output=True, check=True)
    data = plistlib.loads(dec.stdout)
    # These are fake, locally re-signed profiles with no real Apple-issued
    # validity window of their own, so there's no reason their baked-in
    # ExpirationDate should ever be allowed to lapse: bump it fresh on every
    # patch run instead of letting a build start failing once the original
    # date (whatever it happened to be when this profile was captured) is
    # in the past - bazel's ios_extension/ios_application rules reject an
    # expired ExpirationDate outright ("provisioning profile ExpirationDate
    # (...) is in the past"), even for a profile nothing but this script
    # will ever re-verify.
    data['ExpirationDate'] = datetime.datetime.utcnow() + datetime.timedelta(days=3650)
    ent = data.get('Entitlements', {})
    for key in list(ent.keys()):
        v = ent[key]
        if isinstance(v, str) and ORIG in v:
            ent[key] = v.replace(ORIG, NEW)
        elif isinstance(v, list):
            ent[key] = [x.replace(ORIG, NEW) if isinstance(x, str) else x for x in v]
    tmp = tempfile.mktemp(suffix='.plist')
    with open(tmp, 'wb') as f:
        plistlib.dump(data, f, fmt=plistlib.FMT_XML)
    subprocess.run(['security', 'cms', '-S', '-k', 'temp.keychain', '-N', identity, '-i', tmp, '-o', fpath], check=True)
    os.unlink(tmp)
    print(f'Patched {fname}')
