# pkg-rpm-camx-firmware-kodiak

RPM packaging for the Qualcomm Linux CamX camera stack firmware on the Kodiak
platform.

This repository contains RPM packaging rules and scripts for the prebuilt CamX
firmware binaries used by Kodiak (QCM6490). The firmware payload is repackaged
unchanged from the prebuilt release and installed for the Kodiak camera
subsystem.

The prebuilt CamX camera framework binaries are available from
[QArtifactory](https://qartifactory-edge.qualcomm.com/ui/native/qsc_releases/software/chip/component/camx.qclinux.0.0/).

The `c10s` branch contains the RPM packaging files. The `main` branch contains
repository documentation and workflow support files.

## Repository Layout

| File | Purpose |
|---|---|
| `camx-firmware-kodiak.spec` | Builds the Kodiak CamX firmware RPM. |
| `sources` | SHA-512 checksum for the prebuilt firmware archive. |
| `README.md` | Package and repository documentation. |
| `LICENSE.txt` | License for the RPM packaging repository. |

The prebuilt archive is not committed to this repository. `Source0` in the spec
points to the QArtifactory release, and the checksum in `sources` is verified
before the RPM is built.

## CI Workflows

The GitHub Actions workflows use the shared
[`qcom-rpm-utils`](https://github.com/qualcomm-linux/qcom-rpm-utils) build
environment and run `rpmbuild` inside the prebuilt `rpm-builder` container.

| Workflow | Trigger | Purpose |
|---|---|---|
| [`build-on-pr.yml`](.github/workflows/build-on-pr.yml) | Pull request | Downloads and verifies the prebuilt archive, then builds the RPM. |
| [`pkg-release.yml`](.github/workflows/pkg-release.yml) | Manual dispatch | Builds and publishes the RPM to Artifactory after approval. |

Pull requests for the CentOS Stream 10 package must target the `c10s` branch.

## Package

### `camx-firmware-kodiak`

Contains the prebuilt Hexagon DSP firmware image for the Kodiak camera
subsystem:

```text
/usr/lib/firmware/qcom/qcm6490/CAMERA_ICP_170.elf
```

The firmware is installed as-is from the prebuilt release. This RPM contains
no source code and is built for `aarch64` systems.

## Installation

Install the firmware package from the configured CentOS Stream 10 repository:

```bash
sudo dnf install camx-firmware-kodiak
```

## Updating the Package Version

1. Update `Version:` and `upstream_tag` in `camx-firmware-kodiak.spec`.
2. Update the `Source0` archive reference when the prebuilt release changes.
3. Regenerate the source checksum:

   ```bash
   sha512sum --tag camx-firmware-kodiak-<version>_<release>.aarch64.tar.gz > sources
   ```

4. Commit the spec and `sources`, then open a pull request against `c10s`.
5. After the pull request is merged, run `pkg-release.yml` to publish the RPM.

## License

This project is licensed under the BSD 3-Clause License. See [LICENSE.txt](LICENSE.txt) for the complete license text.
