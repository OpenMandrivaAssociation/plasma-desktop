%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: plasma6-desktop
Version: 6.3.2
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/plasma-desktop/-/archive/%{gitbranch}/plasma-desktop-%{gitbranchd}.tar.bz2#/plasma-desktop-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/plasma-desktop-%{version}.tar.xz
%endif
Patch1: plasma-desktop-default-to-kicker.patch
Patch2: taskmanager-config.patch
Patch4: plasma-desktop-5.5.3-use-openmandriva-settings.patch
Summary: KDE Frameworks 6 Plasma-desktop framework
URL: https://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(LibKWorkspace) >= 5.94.0
BuildRequires: cmake(LibColorCorrect) >= 5.94.0
BuildRequires: cmake(LibTaskManager) >= 5.94.0
BuildRequires: cmake(KWinDBusInterface) = %{version}
BuildRequires: cmake(ScreenSaverDBusInterface) = %{version}
BuildRequires: cmake(KRunnerAppDBusInterface) = %{version}
BuildRequires: cmake(KSMServerDBusInterface) = %{version}
BuildRequires: cmake(KSysGuard) >= 5.27.80
BuildRequires: cmake(PlasmaActivitiesStats)
BuildRequires: cmake(KF6QQC2DesktopStyle)
BuildRequires: cmake(KF6Baloo)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(Plasma) >= 5.90.0
BuildRequires: cmake(PlasmaQuick) >= 5.90.0
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Attica)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6Runner)
BuildRequires: cmake(KF6People)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6KDED)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(Plasma5Support)
BuildRequires: cmake(KF6Svg)
BuildRequires: pkgconfig(libaccounts-glib)
BuildRequires: pkgconfig(signon-oauth2plugin)
BuildRequires: cmake(SDL2)
BuildRequires: cmake(LibNotificationManager)
BuildRequires: cmake(Phonon4Qt6)
BuildRequires: cmake(PulseAudio)
BuildRequires: cmake(packagekitqt6)
BuildRequires: cmake(GLIB2)
BuildRequires: cmake(KF6UserFeedback)
BuildRequires: cmake(AccountsQt6)
BuildRequires: cmake(KAccounts6)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libusb)
BuildRequires: pkgconfig(phonon4qt6)
BuildRequires: pkgconfig(libwacom)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core5Compat)
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
BuildRequires: pkgconfig(xkbregistry)
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
BuildRequires: cmake(KPipeWire)
BuildRequires: cmake(WaylandProtocols)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6KIO)
BuildRequires: %mklibname -d KF6IconWidgets
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: boost-devel
BuildRequires: intltool
BuildRequires: xdg-user-dirs
# For DBus interface files
BuildRequires: plasma6-kwin
Recommends: (plasma6-kde-gtk-config if %{_lib}gtk3_0)
Requires: openmandriva-kde-translation
Requires: kf6-plasma-framework
# (tpg) needed for kcm_nightcolor
Requires: gpsd
Supplements: task-plasma6-minimal
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE Frameworks 6 Plasma-desktop framework.

%package -n plasma6-sddm-theme-breeze
Summary: KDE Breeze theme for the SDDM display manager
Group: Graphical desktop/KDE
Requires: plasma6-sddm
Requires: qml-org.kde.breeze.components >= 6.1.0
Requires: qml-org.kde.plasma.private.sessions >= 6.1.0
Requires: qml-org.kde.plasma.workspace >= 6.1.0
Requires: qml(org.kde.plasma.plasma5support)

%description -n plasma6-sddm-theme-breeze
KDE Breeze theme for the SDDM display manager.


%install -a
# (tpg) use layout.js and kde-mimeapps.list from distro-plasma-config
rm -f %{buildroot}%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/layout.js \
	%{buildroot}%{_datadir}/applications/kde-mimeapps.list

desktop-file-install \
		--set-key="NoDisplay" --set-value="true" \
		--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/org.kde.plasma.emojier.desktop

echo '%dir %{_datadir}/plasma/emoji' >>%{name}.lang
for i in %{buildroot}%{_datadir}/plasma/emoji/*.dict; do
	echo "%%lang($(basename $i .dict)) %{_datadir}/plasma/emoji/$(basename $i)" >>%{name}.lang
done

# sddm breeze theme background
sed -i -e "s#^background=.*#background=%{_datadir}/mdk/backgrounds/OpenMandriva-splash.png#" %{buildroot}%{_datadir}/sddm/themes/breeze/theme.conf
sed -i -e "s#^type=.*#type=image#" %{buildroot}%{_datadir}/sddm/themes/breeze/theme.conf

%files -f %{name}.lang
%{_datadir}/knsrcfiles/ksplash.knsrc
%{_bindir}/solid-action-desktop-gen
%{_bindir}/kaccess
%{_bindir}/kcm-touchpad-list-devices
%{_bindir}/knetattach
%{_bindir}/kapplymousetheme
%{_bindir}/plasma-emojier
%{_libdir}/libexec/kf6/kauth/kcmdatetimehelper
%{_qtdir}/plugins/kf6/kded/*.so
%{_qtdir}/qml/org/kde/plasma/private/pager
%{_qtdir}/qml/org/kde/plasma/private/taskmanager
%{_qtdir}/qml/org/kde/plasma/private/trash
%{_qtdir}/qml/org/kde/plasma/activityswitcher
%{_qtdir}/qml/org/kde/private/desktopcontainment
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/org.kde.knetattach.desktop
%{_datadir}/applications/org.kde.plasma.emojier.desktop
%{_datadir}/config.kcfg/*
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/system-services/*
%{_iconsdir}/hicolor/*/*/*.*[g-z]
%{_datadir}/kcmkeys
%{_datadir}/kcmsolidactions
%{_datadir}/kcmmouse
%{_datadir}/kglobalaccel/org.kde.plasma.emojier.desktop
%{_datadir}/knotifications6/*.notifyrc
%{_datadir}/plasma/layout-templates
%dir %{_datadir}/plasma/packages
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
%{_datadir}/solid/devices
%{_qtdir}/qml/org/kde/plasma/private/showdesktop
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmclock.conf
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
%{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall
%{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop
%{_bindir}/tastenbrett
%{_sysconfdir}/xdg/autostart/kaccess.desktop
%{_datadir}/qlogging-categories6/kcmkeys.categories
%{_datadir}/qlogging-categories6/kcm_touchscreen.categories
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel
%{_qtdir}/qml/org/kde/plasma/private/kimpanel
%{_qtdir}/plugins/kf6/krunner
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
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardlayout
%{_datadir}/plasma/plasmoids/org.kde.plasma.marginsseparator
%{_qtdir}/qml/org/kde/plasma/emoji
%{_datadir}/qlogging-categories6/kcm_kded.categories
%{_datadir}/qlogging-categories6/kcm_keyboard.categories
%{_datadir}/qlogging-categories6/kcm_mouse.categories
%{_qtdir}/plugins/plasma/kcminit/kcm_mouse_init.so
%{_qtdir}/plugins/plasma/kcminit/kcm_touchpad_init.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_access.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_baloofile.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_componentchooser.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_kded.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_keyboard.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_keys.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_landingpage.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_mouse.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_smserver.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_splashscreen.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_tablet.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_touchpad.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_touchscreen.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_workspace.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_device_automounter.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_qtquicksettings.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_solid_actions.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcmspellchecking.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_gamecontroller.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_clock.so
%{_datadir}/applications/kcm_clock.desktop
%{_datadir}/applications/kcm_gamecontroller.desktop
%{_datadir}/applications/kcm_access.desktop
%{_datadir}/applications/kcm_activities.desktop
%{_datadir}/applications/kcm_baloofile.desktop
%{_datadir}/applications/kcm_componentchooser.desktop
%{_datadir}/applications/kcm_desktoppaths.desktop
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
%{_datadir}/qlogging-categories6/kcm_gamecontroller.categories
%{_datadir}/qlogging-categories6/kcm_tablet.categories
%{_qtdir}/plugins/plasma/kcms/desktop/kcm_krunnersettings.so
%{_datadir}/applications/kcm_krunnersettings.desktop
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_plasmasearch.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_recentFiles.so
%{_datadir}/applications/kcm_landingpage.desktop
%{_datadir}/applications/kcm_recentFiles.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_activities.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_desktoppaths.so
%{_qtdir}/qml/org/kde/plasma/private/kcm_keyboard/libkcm_keyboard_declarative.so
%{_qtdir}/qml/org/kde/plasma/private/kcm_keyboard/qmldir
%{_datadir}/applications/kaccess.desktop
%{_datadir}/kcm_recentFiles
%{_qtdir}/plugins/attica_kde.so
%dir %{_datadir}/accounts/providers
%dir %{_datadir}/accounts/providers/kde
%{_datadir}/accounts/providers/kde/opendesktop.provider
%{_datadir}/accounts/services/kde/opendesktop-rating.service
%{_prefix}/lib/systemd/user/plasma-kaccess.service

%files -n plasma6-sddm-theme-breeze
%{_datadir}/sddm/themes/breeze
