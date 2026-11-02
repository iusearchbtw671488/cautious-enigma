#!/bin/bash

export TELEGRAM_ENV_SET="1"

export DEVELOPMENT_CODE_SIGN_IDENTITY="iPhone Distribution: Digital Fortress LLC (C67CF9S4VU)"
export DISTRIBUTION_CODE_SIGN_IDENTITY="iPhone Distribution: Digital Fortress LLC (C67CF9S4VU)"
export DEVELOPMENT_TEAM="C67CF9S4VU"

export API_ID="8"
export API_HASH="7245de8e747a0d6fbe11f7cc14fcc0bb"

export BUNDLE_ID="ph.stogra.stograph"
export APP_CENTER_ID="0"
export IS_INTERNAL_BUILD="false"
export IS_APPSTORE_BUILD="true"
export APPSTORE_ID="686449807"
export APP_SPECIFIC_URL_SCHEME="tgapp"
export PREMIUM_IAP_PRODUCT_ID="org.telegram.telegramPremium.monthly"

if [ -z "$BUILD_NUMBER" ]; then
	echo "BUILD_NUMBER is not defined"
	exit 1
fi

export DEVELOPMENT_PROVISIONING_PROFILE_APP="match Development ph.stogra.stograph"
export DISTRIBUTION_PROVISIONING_PROFILE_APP="match AppStore ph.stogra.stograph"
export DEVELOPMENT_PROVISIONING_PROFILE_EXTENSION_SHARE="match Development ph.stogra.stograph.Share"
export DISTRIBUTION_PROVISIONING_PROFILE_EXTENSION_SHARE="match AppStore ph.stogra.stograph.Share"
export DEVELOPMENT_PROVISIONING_PROFILE_EXTENSION_WIDGET="match Development ph.stogra.stograph.Widget"
export DISTRIBUTION_PROVISIONING_PROFILE_EXTENSION_WIDGET="match AppStore ph.stogra.stograph.Widget"
export DEVELOPMENT_PROVISIONING_PROFILE_EXTENSION_NOTIFICATIONSERVICE="match Development ph.stogra.stograph.NotificationService"
export DISTRIBUTION_PROVISIONING_PROFILE_EXTENSION_NOTIFICATIONSERVICE="match AppStore ph.stogra.stograph.NotificationService"
export DEVELOPMENT_PROVISIONING_PROFILE_EXTENSION_NOTIFICATIONCONTENT="match Development ph.stogra.stograph.NotificationContent"
export DISTRIBUTION_PROVISIONING_PROFILE_EXTENSION_NOTIFICATIONCONTENT="match AppStore ph.stogra.stograph.NotificationContent"
export DEVELOPMENT_PROVISIONING_PROFILE_EXTENSION_INTENTS="match Development ph.stogra.stograph.SiriIntents"
export DISTRIBUTION_PROVISIONING_PROFILE_EXTENSION_INTENTS="match AppStore ph.stogra.stograph.SiriIntents"
export DEVELOPMENT_PROVISIONING_PROFILE_WATCH_APP="match Development ph.stogra.stograph.watchkitapp"
export DISTRIBUTION_PROVISIONING_PROFILE_WATCH_APP="match AppStore ph.stogra.stograph.watchkitapp"
export DEVELOPMENT_PROVISIONING_PROFILE_WATCH_EXTENSION="match Development ph.stogra.stograph.watchkitapp.watchkitextension"
export DISTRIBUTION_PROVISIONING_PROFILE_WATCH_EXTENSION="match AppStore ph.stogra.stograph.watchkitapp.watchkitextension"

BUILDBOX_DIR="buildbox"

export CODESIGNING_PROFILES_VARIANT="appstore"

$@
