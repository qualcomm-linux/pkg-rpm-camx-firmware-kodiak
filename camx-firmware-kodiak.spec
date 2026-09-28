%global debug_package %{nil}
%global __os_install_post %{nil}

%global upstream_tag 260925
%global payload_release 1
%global payload_distro el10

Name:           camx-firmware-kodiak
Version:        1.0.8
Release:        1%{?dist}
Summary:        Qualcomm CamX camera stack firmware package (prebuilt payload)
License:        LicenseRef-Qualcomm-nologin-binaries-license
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/camx.qclinux.0.0/%{upstream_tag}/prebuilt_rpm/%{name}-%{version}_%{payload_release}.%{payload_distro}.aarch64.tar.gz
ExclusiveArch:  aarch64

%description
Qualcomm CamX camera stack firmware package.

Prebuilt Hexagon DSP (ICP) firmware image for the Kodiak (qcm6490) camera
subsystem, repackaged unchanged from Stage 1's build output. Contains no
source; the firmware ELF is installed as-is under
/usr/lib/firmware/qcom/qcm6490/.

%prep
%setup -q -n %{name}-%{version}

%build

%install
cp -a usr %{buildroot}/

%files
%dir %{_defaultlicensedir}/%{name}
%license %{_defaultlicensedir}/%{name}/LICENSE.qcom-2
%doc %{_docdir}/%{name}/NOTICE
%dir %{_prefix}/lib/firmware/qcom
%dir %{_prefix}/lib/firmware/qcom/qcm6490
%{_prefix}/lib/firmware/qcom/qcm6490/CAMERA_ICP_170.elf

%changelog
* Mon Sep 28 2026 Qualcomm Camera Team <camx.deb.maintainers@qti.qualcomm.com> - 1.0.8-1
- Initial RPM packaging-only release for the prebuilt Kodiak firmware payload.
