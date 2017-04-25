%define _disable_lto 1
%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma-desktop
Version: 5.9.5
Release: 1
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
BuildRequires: cmake(KDecoration2)
BuildRequires: cmake(LibKWorkspace)
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
BuildRequires: cmake(KDED)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5Notifications)
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
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-shm)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xcb-xinput)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xorg-evdev)
BuildRequires: pkgconfig(xorg-synaptics)
BuildRequires: pkgconfig(xorg-server)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(scim)
BuildRequires: boost-devel
Requires: openmandriva-kde-translation
Suggests: distro-plasma-config
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

%description
KDE Frameworks 5 Plasma-desktop framework.

#----------------------------------------------------------------------------

%define kfontinst_major 5
%define libkfontinst %mklibname kfontinst %{kfontinst_major}

%package -n %{libkfontinst}
Summary:	Plasma 5 desktop shared library
Group:		System/Libraries

%description -n %{libkfontinst}
Plasma 5 desktop shared library.

%files -n %{libkfontinst}
%{_libdir}/libkfontinst.so.%{kfontinst_major}*

#----------------------------------------------------------------------------

%define kfontinstui_major 5
%define libkfontinstui %mklibname kfontinstui %{kfontinstui_major}

%package -n %{libkfontinstui}
Summary:	Plasma 5 desktop shared library
Group:		System/Libraries

%description -n %{libkfontinstui}
Plasma 5 desktop shared library.

%files -n %{libkfontinstui}
%{_libdir}/libkfontinstui.so.%{kfontinstui_major}*

%prep
%setup -qn %{name}-%{plasmaver}
%apply_patches

# We need to increase template depth to make Boost happy
export CXXFLAGS="%{optflags} -ftemplate-depth=1024"
%ifarch %arm
export C=gcc
export CXX=g++
%endif
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# We don't have headers
rm -f %{buildroot}%{_libdir}/libkfontinst.so
rm -f %{buildroot}%{_libdir}/libkfontinstui.so

# (tpg) use layout.js from distro-plasma-config
rm -f %{buildroot}%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/layout.js

%find_lang attica_kde || touch attica_kde.lang
%find_lang joystick || touch joystick.lang
%find_lang kaccess || touch kaccess.lang
%find_lang kcm_activities5 || touch kcm_activities5.lang
%find_lang kcm_device_automounter || touch kcm_device_automounter.lang
%find_lang kcm_activities || touch kcm_activities.lang
%find_lang kcm_autostart || touch kcm_autostart.lang
%find_lang kcm_baloofile || touch kcm_baloofile.lang
%find_lang kcm_desktoppaths || touch kcm_desktoppaths.lang
%find_lang kcm_desktoptheme || touch kcm_desktoptheme.lang
%find_lang kcm_desktopthemedetails || touch kcm_desktopthemedetails.lang
%find_lang kcm_emoticons || touch kcm_emoticons.lang
%find_lang kcm_lookandfeel || touch kcm_lookandfeel.lang
%find_lang kcm_phonon || touch kcm_phonon.lang
%find_lang kcm_search || touch kcm_search.lang
%find_lang kcm_solid_actions || touch kcm_solid_actions.lang
%find_lang kcm_splashscreen || touch kcm_splashscreen.lang
%find_lang kcm_standard_actions || touch kcm_standard_actions.lang
%find_lang kcm_touchpad || touch kcm_touchpad.lang
%find_lang kcmaccess || touch kcmaccess.lang 
%find_lang kcmcolors || touch kcmcolors.lang
%find_lang kcmcomponentchooser || touch kcmcomponentchooser.lang
%find_lang kcmfonts || touch kcmfonts.lang
%find_lang kcmformats || touch kcmformats.lang
%find_lang kcmicons || touch kcmicons.lang
%find_lang kcminput || touch kcminput.lang
%find_lang kcmkclock || touch kcmkclock.lang
%find_lang kcmkded || touch kcmkded.lang
%find_lang kcmkeyboard || touch kcmkeyboard.lang
%find_lang kcmkeys || touch kcmkeys.lang
%find_lang kcmlaunch || touch kcmlaunch.lang
%find_lang kcmmousetheme || touch kcmmousetheme.lang
%find_lang kcmnotify || touch kcmnotify.lang
%find_lang kcmsmserver || touch kcmsmserver.lang
%find_lang kcmstyle || touch kcmstyle.lang
%find_lang kcmtranslations || touch kcmtranslations.lang
%find_lang kcmworkspaceoptions || touch kcmworkspaceoptions.lang
%find_lang kfontinst || touch kfontinst.lang
%find_lang knetattach || touch knetattach.lang
%find_lang krdb || touch krdb.lang
%find_lang plasma_applet_org.kde.desktopcontainment || touch plasma_applet_org.kde.desktopcontainment.lang
%find_lang plasma_applet_org.kde.plasma.kicker || touch plasma_applet_org.kde.plasma.kicker.lang
%find_lang plasma_applet_org.kde.plasma.kickoff || touch plasma_applet_org.kde.plasma.kickoff.lang
%find_lang plasma_applet_org.kde.kimpanel || touch plasma_applet_org.kde.kimpanel.lang
%find_lang plasma_applet_org.kde.plasma.pager || touch plasma_applet_org.kde.plasma.pager.lang
%find_lang plasma_applet_org.kde.plasma.showActivityManager || touch plasma_applet_org.kde.plasma.showActivityManager.lang
%find_lang plasma_applet_org.kde.plasma.taskmanager || touch plasma_applet_org.kde.plasma.taskmanager.lang
%find_lang plasma_applet_org.kde.plasma.trash || touch plasma_applet_org.kde.plasma.trash.lang
%find_lang plasma_applet_org.kde.plasma.windowlist || touch plasma_applet_org.kde.plasma.windowlist.lang
%find_lang plasma_applet_touchpad || touch plasma_applet_touchpad.lang
%find_lang plasma_runner_plasma-desktop || touch plasma_runner_plasma-desktop.lang
%find_lang plasma_runner_kwin || touch plasma_runner_kwin.lang
%find_lang plasma_shell_org.kde.plasma.desktop || touch plasma_shell_org.kde.plasma.desktop.lang
%find_lang plasma_toolbox_org.kde.desktoptoolbox || touch plasma_toolbox_org.kde.dekstoptoolbox.lang
%find_lang plasmaactivitymanager || touch plasmaactivitymanager.lang
%find_lang useraccount || touch useraccount.lang

cat *.lang >%{name}.lang

%files -f %{name}.lang
%{_sysconfdir}/dbus-1/system.d/org.kde.fontinst.conf
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmclock.conf
%{_sysconfdir}/xdg/colorschemes.knsrc
%{_sysconfdir}/xdg/emoticons.knsrc
%{_sysconfdir}/xdg/icons.knsrc
%{_sysconfdir}/xdg/kfontinst.knsrc
%{_sysconfdir}/xdg/plasma-themes.knsrc
%{_sysconfdir}/xdg/xcursor.knsrc
%{_sysconfdir}/xdg/lookandfeel.knsrc
%{_bindir}/solid-action-desktop-gen
%{_bindir}/kaccess
%{_bindir}/kapplymousetheme
%{_bindir}/kcolorschemeeditor
%{_bindir}/kcm-touchpad-list-devices
%{_bindir}/kfontinst
%{_bindir}/kfontview
%{_bindir}/knetattach
%{_bindir}/krdb
%{_libdir}/kconf_update_bin/*
%{_libdir}/libexec/kauth/fontinst
%{_libdir}/libexec/kauth/fontinst_helper
%{_libdir}/libexec/kauth/fontinst_x11
%{_libdir}/libexec/kauth/kcmdatetimehelper
%{_libdir}/libexec/kfontprint
%{_libdir}/libexec/kimpanel-ibus-panel
%{_libdir}/libexec/kimpanel-scim-panel
%{_libdir}/libkdeinit5_kaccess.so
# Technically the following 2 should be library packages, but given
# nothing uses them and nothing CAN use them, the separate library
# packages are useless.
%{_libdir}/qt5/plugins/*.so
%{_libdir}/qt5/plugins/kf5/kded/*.so
%{_libdir}/qt5/plugins/kcms/*.so
%{_libdir}/qt5/qml/org/kde/activities
%{_libdir}/qt5/plugins/plasma/dataengine/*.so
%{_libdir}/qt5/qml/org/kde/plasma/private/kicker
%{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel
%{_libdir}/qt5/qml/org/kde/plasma/private/pager
%{_libdir}/qt5/qml/org/kde/plasma/private/taskmanager
%{_libdir}/qt5/qml/org/kde/plasma/private/trash
%{_libdir}/qt5/qml/org/kde/plasma/activityswitcher
%{_libdir}/qt5/qml/org/kde/private/desktopcontainment
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/org.kde.kfontview.desktop
%{_datadir}/applications/org.kde.knetattach.desktop
%{_datadir}/applications/org.kde.kcolorschemeeditor.desktop
%{_datadir}/color-schemes
%{_datadir}/config.kcfg/*
%{_datadir}/dbus-1/services/*
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/system-services/*
%{_iconsdir}/hicolor/*/*/*.*[g-z]
%{_datadir}/kcm_componentchooser
%{_datadir}/kcm_phonon
%{_datadir}/kcminput
%{_datadir}/kcmkeyboard
%{_datadir}/kcmkeys
%{_datadir}/kcmsolidactions
%{_datadir}/kconf_update/*
%{_datadir}/kcontrol
%{_datadir}/kdisplay
%{_datadir}/kfontinst
%{_datadir}/knotifications5/*.notifyrc
%{_datadir}/konqsidebartng
%{_datadir}/kpackage/kcms/kcm_desktoptheme
%{_datadir}/kpackage/kcms/kcm_lookandfeel
%{_datadir}/kpackage/kcms/kcm_splashscreen
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/kded/*.desktop
%{_datadir}/kservicetypes5/solid-device-type.desktop
%dir %{_datadir}/kf5/kactivitymanagerd
%{_datadir}/kf5/kactivitymanagerd/workspace
%{_datadir}/kservices5/ServiceMenus/installfont.desktop
%{_datadir}/kservices5/fonts.protocol
%{_datadir}/kxmlgui5/kfontinst
%{_datadir}/kxmlgui5/kfontview
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
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel
%{_datadir}/plasma/shells
%{_datadir}/plasma/services/touchpad.operations
%{_datadir}/plasma/services/kimpanel.operations
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
%{_datadir}/solid/devices

%doc %{_docdir}/HTML/*/kcontrol
%doc %{_docdir}/HTML/*/kfontview
%doc %{_docdir}/HTML/*/knetattach
%doc %{_docdir}/HTML/*/plasma-desktop

%lang(sr) %{_datadir}/locale/sr/LC_SCRIPTS/kfontinst/kfontinst.js
%lang(sr@ijekavian) %{_datadir}/locale/sr@ijekavian/LC_SCRIPTS/kfontinst/kfontinst.js
%lang(sr@ijekavianlatin) %{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS/kfontinst/kfontinst.js
%lang(sr@latin) %{_datadir}/locale/sr@latin/LC_SCRIPTS/kfontinst/kfontinst.js
