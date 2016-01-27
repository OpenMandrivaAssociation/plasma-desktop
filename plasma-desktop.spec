%define _disable_lto 1
%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma-desktop
Version: 5.5.4
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
Group: System/Libraries
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5)
BuildRequires: cmake(KDecoration2)
BuildRequires: cmake(LibKWorkspace)
BuildRequires: cmake(LibTaskManager)
BuildRequires: cmake(KWinDBusInterface)
BuildRequires: cmake(ScreenSaverDBusInterface)
BuildRequires: cmake(KRunnerAppDBusInterface)
BuildRequires: cmake(KSMServerDBusInterface)
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

%description
KDE Frameworks 5 Plasma-desktop framework.

%define KF5ActivitiesExperimentalStats_major 1
%define libKF5ActivitiesExperimentalStats %mklibname KF5ActivitiesExperimentalStats %{KF5ActivitiesExperimentalStats_major}

%package -n %{libKF5ActivitiesExperimentalStats}
Summary:	Plasma 5 desktop shared library
Group:		System/Libraries

%description -n %{libKF5ActivitiesExperimentalStats}
Plasma 5 desktop shared library.

%files -n %{libKF5ActivitiesExperimentalStats}
%{_libdir}/libKF5ActivitiesExperimentalStats.so.%{KF5ActivitiesExperimentalStats_major}*
%{_libdir}/libKF5ActivitiesExperimentalStats.so.0.0.1

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

%find_lang attica_kde
%find_lang joystick
%find_lang kaccess
%find_lang kcm_device_automounter
%find_lang kcm_autostart
%find_lang kcm_baloofile
%find_lang kcm_desktoppaths
%find_lang kcm_desktopthemedetails
%find_lang kcm_emoticons
%find_lang kcm_lookandfeel
%find_lang kcm_phonon
%find_lang kcm_search
%find_lang kcm_solid_actions
%find_lang kcm_splashscreen
%find_lang kcm_standard_actions
%find_lang kcm_touchpad
%find_lang kcmaccess
%find_lang kcmcolors
%find_lang kcmcomponentchooser
%find_lang kcmfonts
%find_lang kcmformats
%find_lang kcmicons
%find_lang kcminput
%find_lang kcmkclock
%find_lang kcmkded
%find_lang kcmkeyboard
%find_lang kcmkeys
%find_lang kcmlaunch
%find_lang kcmmousetheme
%find_lang kcmnotify
%find_lang kcmsmserver
%find_lang kcmstyle
%find_lang kcmtranslations
%find_lang kcmworkspaceoptions
%find_lang kfontinst
%find_lang knetattach
%find_lang krdb
%find_lang plasma_applet_org.kde.desktopcontainment
%find_lang plasma_applet_org.kde.plasma.kicker
%find_lang plasma_applet_org.kde.plasma.kickoff
%find_lang plasma_applet_org.kde.plasma.pager
%find_lang plasma_applet_org.kde.plasma.showActivityManager
%find_lang plasma_applet_org.kde.plasma.taskmanager
%find_lang plasma_applet_org.kde.plasma.trash
%find_lang plasma_applet_org.kde.plasma.windowlist
%find_lang plasma_applet_touchpad
%find_lang plasma_runner_plasma-desktop
%find_lang plasma_shell_org.kde.plasma.desktop
%find_lang plasma_toolbox_org.kde.desktoptoolbox
%find_lang useraccount

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
%{_bindir}/solid-action-desktop-gen
%{_bindir}/kaccess
%{_bindir}/kapplymousetheme
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
%{_libdir}/libkdeinit5_kaccess.so
# Technically the following 2 should be library packages, but given
# nothing uses them and nothing CAN use them, the separate library
# packages are useless.
%{_libdir}/qt5/plugins/*.so
%{_libdir}/qt5/plugins/kf5/kded/*.so
%{_libdir}/qt5/plugins/kcms/*.so
%{_libdir}/qt5/plugins/plasma/dataengine/*.so
%{_libdir}/qt5/qml/org/kde/plasma/private/kicker
%{_libdir}/qt5/qml/org/kde/plasma/private/pager
%{_libdir}/qt5/qml/org/kde/plasma/private/taskmanager
%{_libdir}/qt5/qml/org/kde/plasma/private/trash
%{_libdir}/qt5/qml/org/kde/plasma/activityswitcher
%{_libdir}/qt5/qml/org/kde/private/desktopcontainment
%{_datadir}/applications/org.kde.kfontview.desktop
%{_datadir}/applications/org.kde.knetattach.desktop
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
# FIXME do we still need this with sddm? Should we move the icons to
# a more SDDM friendly location?
%{_datadir}/kdm
%{_datadir}/kfontinst
%{_datadir}/knotifications5/*.notifyrc
%{_datadir}/konqsidebartng
%{_datadir}/kpackage/kcms/kcm_lookandfeel
%{_datadir}/kpackage/kcms/kcm_splashscreen
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/kded/*.desktop
%{_datadir}/kservicetypes5/solid-device-type.desktop
%dir %{_datadir}/ksmserver/windowmanagers
%{_datadir}/ksmserver/windowmanagers/*.desktop
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
%{_datadir}/plasma/shells
%{_datadir}/plasma/services/touchpad.operations
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
%{_datadir}/solid/devices

%doc %{_docdir}/HTML/*/kcontrol
%doc %{_docdir}/HTML/*/kfontview
%doc %{_docdir}/HTML/*/knetattach
%doc %{_docdir}/HTML/*/plasma-desktop
