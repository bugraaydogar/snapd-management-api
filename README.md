# snapd-management-snap

This is a sample REST API that works as a proxy by communicating with snapd's rest api
provided via a unix socket.

## Build and Install

    ```
    $ snapcraft --use-lxd
    $ sudo snap install snapd-management-snap_0.1_amd64.snap --dangerous --devmode
    ```

## Connect Interface

It is not mandatory since you install the snap with `--devmode` but you could connect the interfaces the following command;

    ```
    $ sudo snap connect snapd-management-snap:snapd-control :snapd-control
    ```

## Run
The application starts by using the port 5000.
Open a web browser and go to <your-ip-address>:5000/docs and you could start using it.

