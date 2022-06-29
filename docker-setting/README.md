# Docker上でRaspberrypiを実行する

```
$ wget https://downloads.raspberrypi.org/raspios_lite_arm64/root.tar.xz
$ docker image import ./root.tar.xz raspios_lite_arm64:2022-01-28
$ docker run -it --rm --entrypoint /bin/bash raspios_lite_arm64:2022-01-28
```
