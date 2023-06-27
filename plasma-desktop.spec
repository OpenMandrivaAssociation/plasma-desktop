%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma-desktop
Version: 5.27.6
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Source100: %{name}.rpmlintrc
Patch4: plasma-desktop-5.5.3-use-openmandriva-settings.patch
Summary: KDE Frameworks 5 Plasma-desktop framework
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(AppStreamQt) < 1.0.0
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5)
BuildRequires: cmake(Breeze) < 5.27.50
BuildRequires: cmake(KDecoration2) = %{version}
BuildRequires: cmake(LibKWorkspace) < 5.27.50
BuildRequires: cmake(LibColorCorrect) < 5.27.50
BuildRequires: cmake(LibTaskManager) < 5.27.50
BuildRequires: cmake(KWinEffects) < 5.27.50
BuildRequires: cmake(ScreenSaverDBusInterface)
BuildRequires: cmake(KF5ActivitiesStats)
BuildRequires: cmake(KF5Baloo)
BuildRequires: cmake(KF5ItemModels)
BuildRequires: cmake(KF5Emoticons)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5PlasmaQuick)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5NotifyConfig)
BuildRequires: cmake(KF5Attica)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5Runner)
BuildRequires: cmake(KF5People)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KDED)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5QQC2DeskopStyle)
BuildRequires: cmake(KAccounts)
BuildRequires: cmake(AccountsQt5)
BuildRequires: pkgconfig(libaccounts-glib)
BuildRequires: pkgconfig(signon-oauth2plugin)
BuildRequires: cmake(LibNotificationManager) < 5.27.50
BuildRequires: cmake(Phonon4Qt5)
BuildRequires: cmake(PulseAudio)
BuildRequires: cmake(GLIB2)
BuildRequires: cmake(packagekitqt5)
BuildRequires: cmake(KUserFeedback) < 5.27.50
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libusb)
BuildRequires: pkgconfig(phonon4qt5)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickWidgets)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-shm)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xcb-xinput)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xcb-atom)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xorg-evdev)
BuildRequires: pkgconfig(xorg-synaptics)
BuildRequires: pkgconfig(xorg-server)
BuildRequires: pkgconfig(xorg-libinput)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(scim)
BuildRequires: pkgconfig(udev)
BuildRequires: cmake(KPipeWire) < 5.27.50
BuildRequires: cmake(WaylandProtocols)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: boost-devel
BuildRequires: intltool
BuildRequires: xdg-user-dirs
Requires: openmandriva-kde-translation
Requires: plasma-framework
Requires: kirigami2
# (crazy) crahses without
Requires: qqc2-desktop-style >= %{version}
Recommends: distro-release-desktop-Plasma
# (tpg) needed for kcm_nightcolor
Requires: gpsd
Supplements: task-plasma-minimal

Obsoletes: kdeartwork-emoticons < 1:15.08.3-3
Obsoletes: kdeartwork4-emoticons < 1:4.14.3-3
Provides: kdeartwork-emoticons = 1:15.08.3-3
Provides: kdeartwork4-emoticons = 1:4.14.3-3

Obsoletes: kdeartwork-color-schemes < 1:15.08.3-3
Obsoletes: kdeartwork4-color-schemes < 1:4.14.3-3
Provides: kdeartwork-color-schemes = 1:15.08.3-3
Provides: kdeartwork4-color-schemes = 1:4.14.3-3

Obsoletes: kdeartwork-kscreensaver < 1:15.08.3-3
Obsoletes: kdeartwork4-kscreensaver < 1:4.14.3-3
Provides: kdeartwork-kscreensaver = 1:15.08.3-3
Provides: kdeartwork4-kscreensaver = 1:4.14.3-3

Obsoletes: kdeartwork-styles < 1:15.08.3-3
Obsoletes: kdeartwork4-styles < 1:4.14.3-3
Provides: kdeartwork-styles = 1:15.08.3-3
Provides: kdeartwork4-styles = 1:4.14.3-3

Obsoletes: kdeartwork < 1:15.08.3-3
Obsoletes: kdeartwork4 < 1:4.14.3-3
Provides: kdeartwork = 1:15.08.3-3
Provides: kdeartwork4 = 1:4.14.3-3

Obsoletes: plasma-desktoptheme-androbit < 1:15.08.3-3
Provides: plasma-desktoptheme-androbit = 1:15.08.3-3

Obsoletes: plasma-desktoptheme-aya < 1:15.08.3-3
Provides: plasma-desktoptheme-aya = 1:15.08.3-3

Obsoletes: plasma-desktoptheme-produkt < 1:15.08.3-3
Provides: plasma-desktoptheme-produkt = 1:15.08.3-3

Obsoletes: plasma-desktoptheme-slim-glow < 1:15.08.3-3
Provides: plasma-desktoptheme-slim-glow = 1:15.08.3-3

Obsoletes: plasma-desktoptheme-tibanna < 1:15.08.3-3
Provides: plasma-desktoptheme-tibanna = 1:15.08.3-3

Obsoletes: plasma-applet-touchpad < 1.2
Provides: plasma-applet-touchpad = 1.2

Obsoletes: kcm-touchpad < 1.2
Provides: kcm-touchpad = 1.2

Obsoletes: kcm-touchpad5 < 5.1.95-3
Provides: kcm-touchpad5 = 5.1.95-3

Obsoletes: kactivities-workspace < 5.6.0
Conflicts: kdeplasma-addons <= 5.5.5
Conflicts: kactivitymanagerd < 5.6.0
Conflicts: kdeplasma-addons < 5.16.3

%description
KDE Frameworks 5 Plasma-desktop framework.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# (tpg) use layout.js from distro-plasma-config
rm -f %{buildroot}%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/layout.js

desktop-file-install \
		--set-key="NoDisplay" --set-value="true" \
		--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/org.kde.plasma.emojier.desktop
						
%find_lang %{name} --all-name --with-html

echo '%dir %{_datadir}/plasma/emoji' >>%{name}.lang
for i in %{buildroot}%{_datadir}/plasma/emoji/*.dict; do
	echo "%%lang($(basename $i .dict)) %{_datadir}/plasma/emoji/$(basename $i)" >>%{name}.lang
done

%files -f %{name}.lang
%{_datadir}/knsrcfiles/ksplash.knsrc
%{_bindir}/solid-action-desktop-gen
%{_bindir}/kaccess
%{_bindir}/kcm-touchpad-list-devices
%{_bindir}/knetattach
%{_bindir}/kapplymousetheme
%{_bindir}/plasma-emojier
%{_libdir}/libexec/kauth/kcmdatetimehelper
%{_libdir}/qt5/plugins/*.so
%{_libdir}/qt5/plugins/kf5/kded/*.so
%{_libdir}/qt5/qml/org/kde/activities
%{_libdir}/qt5/plugins/plasma/dataengine/*.so
%{_libdir}/qt5/qml/org/kde/plasma/private/pager
%{_libdir}/qt5/qml/org/kde/plasma/private/taskmanager
%{_libdir}/qt5/qml/org/kde/plasma/private/trash
%{_libdir}/qt5/qml/org/kde/plasma/activityswitcher
%{_libdir}/qt5/qml/org/kde/private/desktopcontainment
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/org.kde.knetattach.desktop
%{_datadir}/applications/org.kde.plasma.emojier.desktop
%{_datadir}/accounts/providers/kde/opendesktop.provider
%{_datadir}/accounts/services/kde/opendesktop-rating.service
%{_datadir}/config.kcfg/*
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/system-services/*
%{_iconsdir}/hicolor/*/*/*.*[g-z]
%{_datadir}/kcmkeys
%{_datadir}/kcmsolidactions
%{_datadir}/kcmmouse
%{_datadir}/kconf_update/*
%{_datadir}/kglobalaccel/org.kde.plasma.emojier.desktop
%{_datadir}/knotifications5/*.notifyrc
%{_datadir}/kpackage/kcms/kcm_baloofile
%{_datadir}/kpackage/kcms/kcm_splashscreen
%{_datadir}/kpackage/kcms/kcm_workspace
%{_datadir}/kservicetypes5/solid-device-type.desktop
%dir %{_datadir}/kf5/kactivitymanagerd
%{_datadir}/kf5/kactivitymanagerd/workspace
%{_datadir}/plasma/layout-templates
%dir %{_datadir}/plasma/packages
%{_datadir}/plasma/packages/org.kde.desktoptoolbox
%{_datadir}/plasma/packages/org.kde.paneltoolbox
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment
%{_datadir}/plasma/plasmoids/org.kde.panel
%{_datadir}/plasma/plasmoids/org.kde.plasma.folder
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff
%{_datadir}/plasma/plasmoids/org.kde.plasma.icontasks
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager
%{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager
%{_datadir}/plasma/plasmoids/org.kde.plasma.trash
%{_datadir}/plasma/plasmoids/org.kde.plasma.windowlist
%{_datadir}/plasma/shells
%{_datadir}/plasma/services/touchpad.operations
%{_datadir}/solid/devices
%{_libdir}/qt5/qml/org/kde/plasma/private/showdesktop
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmclock.conf
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
%{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall
%{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop
%{_bindir}/tastenbrett
%{_sysconfdir}/xdg/autostart/kaccess.desktop
%{_datadir}/kpackage/kcms/kcm5_kded
%{_datadir}/kpackage/kcms/kcm_keys
%{_datadir}/qlogging-categories5/kcmkeys.categories
%{_datadir}/qlogging-categories5/kcm_touchscreen.categories
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel
%{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel
%{_libdir}/qt5/plugins/kf5/krunner
%{_libdir}/libexec/kimpanel-ibus-panel
%{_libdir}/libexec/kimpanel-ibus-panel-launcher
%{_libdir}/libexec/kimpanel-scim-panel
#%{_datadir}/accounts/providers/kde/opendesktop.provider
#%{_datadir}/accounts/services/kde/opendesktop-rating.service
%lang(sr) %{_datadir}/locale/sr/LC_SCRIPTS/kfontinst
%lang(sr@ijekavian) %{_datadir}/locale/sr@ijekavian/LC_SCRIPTS/kfontinst
%lang(sr@ijekavianlatin) %{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS/kfontinst
%lang(sr@latin) %{_datadir}/locale/sr@latin/LC_SCRIPTS/kfontinst
%{_bindir}/krunner-plugininstaller
%{_datadir}/knsrcfiles/krunner.knsrc
%{_datadir}/kpackage/kcms/kcm_componentchooser
%{_datadir}/kpackage/kcms/kcm_smserver
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardlayout
%{_datadir}/plasma/plasmoids/org.kde.plasma.marginsseparator
%{_libdir}/qt5/qml/org/kde/plasma/emoji
%{_datadir}/kpackage/kcms/kcm_landingpage
%{_datadir}/qlogging-categories5/kcm_kded.categories
%{_datadir}/qlogging-categories5/kcm_keyboard.categories
%{_datadir}/qlogging-categories5/kcm_mouse.categories
%{_datadir}/plasma/desktoptheme/default/icons/touchpad.svg
%{_datadir}/plasma/plasmoids/touchpad
%{_libdir}/qt5/plugins/plasma/kcminit/kcm_mouse_init.so
%{_libdir}/qt5/plugins/plasma/kcminit/kcm_touchpad_init.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_access.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_baloofile.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_componentchooser.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kded.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_keyboard.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_keys.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_landingpage.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_mouse.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_smserver.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_splashscreen.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_tablet.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_touchpad.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_touchscreen.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_workspace.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_activities.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_clock.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_desktoppaths.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_device_automounter.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_joystick.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_qtquicksettings.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_solid_actions.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcmspellchecking.so
%{_datadir}/applications/kcm_access.desktop
%{_datadir}/applications/kcm_activities.desktop
%{_datadir}/applications/kcm_baloofile.desktop
%{_datadir}/applications/kcm_clock.desktop
%{_datadir}/applications/kcm_componentchooser.desktop
%{_datadir}/applications/kcm_desktoppaths.desktop
%{_datadir}/applications/kcm_joystick.desktop
%{_datadir}/applications/kcm_kded.desktop
%{_datadir}/applications/kcm_keyboard.desktop
%{_datadir}/applications/kcm_keys.desktop
%{_datadir}/applications/kcm_mouse.desktop
%{_datadir}/applications/kcm_plasmasearch.desktop
%{_datadir}/applications/kcm_qtquicksettings.desktop
%{_datadir}/applications/kcm_smserver.desktop
%{_datadir}/applications/kcm_solid_actions.desktop
%{_datadir}/applications/kcm_splashscreen.desktop
%{_datadir}/applications/kcm_tablet.desktop
%{_datadir}/applications/kcm_touchpad.desktop
%{_datadir}/applications/kcm_touchscreen.desktop
%{_datadir}/applications/kcm_workspace.desktop
%{_datadir}/applications/kcmspellchecking.desktop
%{_datadir}/kpackage/kcms/kcm_access
%{_datadir}/kpackage/kcms/kcm_tablet
%{_datadir}/qlogging-categories5/kcm_tablet.categories
%{_datadir}/kpackage/kcms/kcm_touchscreen
%{_libdir}/qt5/plugins/plasma/kcms/desktop/kcm_krunnersettings.so
%{_datadir}/applications/kcm_krunnersettings.desktop
%{_datadir}/kpackage/kcms/kcm_krunnersettings
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_plasmasearch.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_recentFiles.so
%{_datadir}/applications/kcm_landingpage.desktop
%{_datadir}/applications/kcm_recentFiles.desktop
%{_datadir}/kf5/kcm_recentFiles
%{_datadir}/kpackage/kcms/kcm_plasmasearch
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager
