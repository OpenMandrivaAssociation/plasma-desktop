%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma-desktop
Version: 5.20.3
Release: 6
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Source100: %{name}.rpmlintrc
#Patch0: plasma-desktop-5.1.95-clang.patch
#Patch1: plasma-desktop-5.2.2-add-autohint.patch
# Move date and time to more obvious place in system settings
Patch3: plasma-desktop-5.3.1-dateandtime-category.patch
Patch4: plasma-desktop-5.5.3-use-openmandriva-settings.patch
Summary: KDE Frameworks 5 Plasma-desktop framework
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(AppStreamQt)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5)
BuildRequires: cmake(Breeze) >= %(echo %{version} |cut -d. -f1-3)
BuildRequires: cmake(KDecoration2)
BuildRequires: cmake(LibKWorkspace)
BuildRequires: cmake(LibColorCorrect)
BuildRequires: cmake(LibTaskManager)
BuildRequires: cmake(KWinDBusInterface)
BuildRequires: cmake(ScreenSaverDBusInterface)
BuildRequires: cmake(KRunnerAppDBusInterface)
BuildRequires: cmake(KSMServerDBusInterface)
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
BuildRequires: cmake(LibNotificationManager)
BuildRequires: cmake(Phonon4Qt5)
BuildRequires: cmake(PulseAudio)
BuildRequires: cmake(GLIB2)
BuildRequires: cmake(packagekitqt5)
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
BuildRequires: boost-devel
Requires: openmandriva-kde-translation
Requires: plasma-framework
Requires: kirigami2
# (crazy) crahses without
Requires: qqc2-desktop-style >= %{version}
Suggests: distro-plasma-config
# (tpg) needed for kcm_nightcolor
Requires: gpsd

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

#----------------------------------------------------------------------------
%package kcm_users
Summary:	Overly simplistic user manager
Group:		Graphical desktop/KDE

%description kcm_users
Overly simplistic user manager

Among other problems, this user manager lacks support for groups.
It is highly recommended to use om-user-manager, kuser, or command
line tools instead.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# (tpg) use layout.js from distro-plasma-config
rm -f %{buildroot}%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/layout.js

%find_lang %{name} --all-name --with-html
%find_lang kcm_users
cat %{name}.lang kcm_users.lang |sort |uniq >%{name}-except-users.lang

%files kcm_users -f kcm_users.lang
%{_libdir}/qt5/plugins/kcms/kcm_users.so
%{_datadir}/kpackage/kcms/kcm_users
%{_datadir}/kservices5/kcm_users.desktop

%files -f %{name}-except-users.lang
%{_datadir}/knsrcfiles/ksplash.knsrc
%{_bindir}/solid-action-desktop-gen
%{_bindir}/kaccess
%{_bindir}/kcm-touchpad-list-devices
%{_bindir}/knetattach
%{_bindir}/kapplymousetheme
%{_libdir}/libexec/kauth/kcmdatetimehelper
%{_libdir}/libkdeinit5_kaccess.so
%{_libdir}/qt5/plugins/*.so
%{_libdir}/qt5/plugins/kf5/kded/*.so
%{_libdir}/qt5/plugins/kcms/*.so
%exclude %{_libdir}/qt5/plugins/kcms/kcm_users.so
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
%{_datadir}/kcm_componentchooser
%{_datadir}/kcmkeyboard
%{_datadir}/kcmkeys
%{_datadir}/kcmsolidactions
%{_datadir}/kcmmouse
%{_datadir}/kconf_update/*
%{_datadir}/kglobalaccel/org.kde.plasma.emojier.desktop
%{_datadir}/knotifications5/*.notifyrc
%{_datadir}/kpackage/kcms/kcm_baloofile
%{_datadir}/kpackage/kcms/kcm_launchfeedback
%{_datadir}/kpackage/kcms/kcm_nightcolor
%{_datadir}/kpackage/kcms/kcm_splashscreen
%{_datadir}/kpackage/kcms/kcm_workspace
%{_datadir}/kservices5/*.desktop
%exclude %{_datadir}/kservices5/kcm_users.desktop
%{_datadir}/kservices5/kded/*.desktop
%{_datadir}/kservicetypes5/solid-device-type.desktop
%dir %{_datadir}/kf5/kactivitymanagerd
%{_datadir}/kf5/kactivitymanagerd/workspace
%{_datadir}/plasma/layout-templates
%{_datadir}/plasma/desktoptheme
%dir %{_datadir}/plasma/packages
%{_datadir}/plasma/plasmoids/touchpad
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
%{_datadir}/kpackage/kcms/kcm_notifications
%{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall
%{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop
%{_bindir}/ibus-ui-emojier-plasma
%{_bindir}/tastenbrett
%{_sysconfdir}/xdg/autostart/kaccess.desktop
%{_datadir}/kpackage/kcms/kcm_autostart
%{_datadir}/kpackage/kcms/kcm5_kded
%{_datadir}/kpackage/kcms/kcm_keys
%{_datadir}/qlogging-categories5/kcmkeys.categories
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel
%{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel
%{_libdir}/qt5/plugins/kf5/krunner
%{_libdir}/libexec/kimpanel-ibus-panel
%{_libdir}/libexec/kimpanel-ibus-panel-launcher
%{_libdir}/libexec/kimpanel-scim-panel
#%{_datadir}/accounts/providers/kde/opendesktop.provider
#%{_datadir}/accounts/services/kde/opendesktop-rating.service
%{_datadir}/qlogging-categories5/kcmusers.categories
%lang(sr) %{_datadir}/locale/sr/LC_SCRIPTS/kfontinst
%lang(sr@ijekavian) %{_datadir}/locale/sr@ijekavian/LC_SCRIPTS/kfontinst
%lang(sr@ijekavianlatin) %{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS/kfontinst
%lang(sr@latin) %{_datadir}/locale/sr@latin/LC_SCRIPTS/kfontinst
