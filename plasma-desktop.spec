%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: plasma-desktop
Version: 5.1.1
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Source100: %{name}.rpmlintrc
Summary: KDE Frameworks 5 Plasma-desktop framework
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5)
BuildRequires: cmake(KDecorations)
BuildRequires: cmake(LibKWorkspace)
BuildRequires: cmake(LibTaskManager)
BuildRequires: cmake(KWinDBusInterface)
BuildRequires: cmake(ScreenSaverDBusInterface)
BuildRequires: cmake(KRunnerAppDBusInterface)
BuildRequires: cmake(KSMServerDBusInterface)
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
BuildRequires: cmake(Fontconfig)
BuildRequires: cmake(XCB)
BuildRequires: cmake(OpenGL)
BuildRequires: cmake(Freetype)
BuildRequires: cmake(Fontconfig)
BuildRequires: cmake(Strigi)
BuildRequires: cmake(Freetype)
BuildRequires: cmake(Phonon4Qt5)
BuildRequires: cmake(PulseAudio)
BuildRequires: cmake(GLIB2)
BuildRequires: cmake(packagekitqt5)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libusb)
BuildRequires: ninja
BuildRequires: plasma-workspace

%description
KDE Frameworks 5 Plasma-desktop framework

%prep
%setup -qn %{name}-%{plasmaver}
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}
%find_lang attica_kde
%find_lang joystick
%find_lang kaccess
%find_lang kcm_autostart
%find_lang kcm_desktoppaths
%find_lang kcm_desktopthemedetails
%find_lang kcm_emoticons
%find_lang kcm_phonon
%find_lang kcm_solid_actions
%find_lang kcm_standard_actions
%find_lang kcmaccess
%find_lang kcmbell
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
%find_lang kcm_lookandfeel
%find_lang kcmnotify
%find_lang kcm_search
%find_lang kcmsmserver
%find_lang kcmstyle
%find_lang kcmtranslations
%find_lang kcmworkspaceoptions
%find_lang kfontinst
%find_lang knetattach
%find_lang krdb
%find_lang ksplashthemes
%find_lang ktouchpadenabler
%find_lang libkonq || touch libkonq.lang
%find_lang plasma_applet_org.kde.plasma.folder
%find_lang plasma_applet_org.kde.plasma.kicker
%find_lang plasma_applet_org.kde.plasma.kickoff
%find_lang plasma_applet_org.kde.plasma.pager
%find_lang plasma_applet_org.kde.plasma.showActivityManager
%find_lang plasma_applet_org.kde.plasma.taskmanager
%find_lang plasma_applet_org.kde.plasma.trash
%find_lang plasma_applet_org.kde.plasma.windowlist
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
%{_libdir}/libkfontinst.so*
%{_libdir}/libkfontinstui.so*
%{_libdir}/plugins/*.so
%{_libdir}/qml/org/kde/plasma/private/folder
%{_libdir}/qml/org/kde/plasma/private/kicker
%{_libdir}/qml/org/kde/plasma/private/kickoff
%{_libdir}/qml/org/kde/plasma/private/pager
%{_libdir}/qml/org/kde/plasma/private/taskmanager
%{_libdir}/qml/org/kde/plasma/private/trash
%{_datadir}/applications/kfontview.desktop
%{_datadir}/applications/knetattach.desktop
%{_datadir}/color-schemes
%{_datadir}/config.kcfg/*
%{_datadir}/dbus-1/services/*
%{_datadir}/dbus-1/system-services/*
%{_datadir}/icons/*/*/*/kfontview.*
%{_datadir}/icons/*/*/*/fonts-package.*
%{_datadir}/icons/*/*/*/preferences-desktop-font-installer.*
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
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservicetypes5/solid-device-type.desktop
%dir %{_datadir}/ksmserver/windowmanagers
%{_datadir}/ksmserver/windowmanagers/*.desktop
%dir %{_datadir}/kthememanager
%dir %{_datadir}/kthememanager/themes
%{_datadir}/kthememanager/themes/HighContrastDark-big
%{_datadir}/kthememanager/themes/HighContrastDark
%{_datadir}/kthememanager/themes/HighContrastLight-big
%{_datadir}/kthememanager/themes/HighContrastLight
%{_datadir}/kthememanager/themes/KDE_Classic
%{_datadir}/kthememanager/themes/Keramik
%{_datadir}/kthememanager/themes/Plastik
%{_datadir}/kthememanager/themes/Platinum
%{_datadir}/kthememanager/themes/Redmond
%{_datadir}/kthememanager/themes/Sunshine
%{_datadir}/kthememanager/themes/YellowOnBlue-big
%{_datadir}/kthememanager/themes/YellowOnBlue
%{_datadir}/kservices5/ServiceMenus/installfont.desktop
%{_datadir}/kservices5/fonts.protocol
%{_datadir}/kservices5/kded/keyboard.desktop
%{_datadir}/kxmlgui5/kfontinst
%{_datadir}/kxmlgui5/kfontview
%{_datadir}/plasma/kcms/kcm_lookandfeel
%{_datadir}/plasma/layout-templates
%dir %{_datadir}/plasma/packages
%{_datadir}/plasma/packages/org.kde.desktoptoolbox
%{_datadir}/plasma/packages/org.kde.paneltoolbox
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment
%{_datadir}/plasma/plasmoids/org.kde.panel
%{_datadir}/plasma/plasmoids/org.kde.plasma.folder
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager
%{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager
%{_datadir}/plasma/plasmoids/org.kde.plasma.trash
%{_datadir}/plasma/plasmoids/org.kde.plasma.windowlist
%{_datadir}/plasma/shells
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
%{_datadir}/solid/devices
%doc %{_docdir}/HTML/en/kcontrol
%doc %{_docdir}/HTML/en/kfontview
%doc %{_docdir}/HTML/en/knetattach
%doc %{_docdir}/HTML/en/plasma-desktop
