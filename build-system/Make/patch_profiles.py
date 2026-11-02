import os, sys, plistlib, subprocess, tempfile, re

ORIG = 'ph.telegra.Telegraph'
NEW  = 'ph.stogra.stograph'
DIR  = 'build-system/fake-codesigning/profiles'

result = subprocess.run(['security', 'find-identity', '-v', '-p', 'codesigning', 'temp.keychain'],
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
