How to Upgrade Kubuntu 23.10 to 24.04
=====================================

.. post:: Jul 27, 2024
   :tags: upgrade, kubuntu
   :category: Sysadmin
   :author: Marcin Prączko
   :language: eg

Introduction
------------

The moment has arrived to upgrade my laptop from ``Kubuntu 23.10`` to ``Kubuntu 24.04``.
When I received the notification about the new version, I decided it was time to take a big step.
However, the upgrade process was not without its challenges, especially given my laptop's unique configuration.
As is often the case, the standard procedures didn't quite work for me. In this post, I'll share my experiences and solutions,
hoping to make your upgrade journey smoother and more successful.

.. image:: _static/img/upgrade-kubuntu-23.10-to-24.04-plasma-info.jpeg
  :width: 512
  :alt: upgrade-kubuntu-23.10-to-24.04-plasma-info.jpeg
  :name: Upgrade KDE Plasma Notification

Some links which I've used during the upgrade process can be found in :ref:`upgrade-kubuntu-23.10-to-24.04-resources` section below:

- Please check issues which I had during the upgrade process and how I've solved them.
- I've you're thinking that you won't have those issues during the upgrade process, please try follow steps
  from :ref:`upgrade-kubuntu-23.10-to-24.04-resources` section.

.. note::

  I have really hope that this post will be valuable for you during the upgrade process of your ``Kubuntu`` system.

Short Summary
-------------

In this post, I will describe the steps I took to upgrade my laptop from ``Kubuntu 23.10`` to ``Kubuntu 24.04``.

You can expect the following:

- Preparation steps before the upgrade.
- How to move the snap folder to another partition *(related with the challenges of not having enough free space on the root partition)*
- Suprises during working from terminal (no WIFI)
- Some minor issues after the upgrade.

Challenges before the upgrade
-----------------------------

Before starting the upgrade process, I had to face with some challenges:

- I knew that my root partition can have not enough free space.

I had root partition with ``20GB`` and only ``2GB`` free space. This was not enough for the upgrade process.
Reason of so small root partition was that I have separate partition for major folders like ``/home``, ``/usr``.

Long time ago I've decided to have separate partitions for major folders based on my experience and recommendations from the internet.
However, it looks like those days are long gone, as I can see that having a ``20GB`` root partition today is not enough, which is really surprising to me.


Upgrade process - initial steps
-------------------------------

Fistly I wanted to check major details about my operating system, so following is a part of the output from the ``neofetch`` command:

.. literalinclude:: _static/snippets/upgrade-kubuntu-23.10-to-24.04-neofetch01.txt
  :language: text

Secondly I decided that I want to do upgrade from terminal or console running under KDE Plasma.

.. important::

  Finally commands below has been run on console in KDE Plasma (which means on GUI).

Intitial commands
+++++++++++++++++

Following commands were used to start the upgrade process:

.. code-block:: bash

    # Update the package list and prepare for upgrade
    sudo apt-get update && sudo apt-get dist-upgrade

    # Install the update-manager-core package
    sudo apt install update-manager-core

Above commands worked without any issues.

Following command suprised me with many details about distribution.

.. note::

    That was first time in my live when I've done distribution upgrade process on ``Ubuntu/Kubuntu``.

.. code-block:: bash

    # Start the upgrade process
    sudo do-release-upgrade

And this displayed the following message:

.. literalinclude:: _static/snippets/upgrade-kubuntu-23.10-to-24.04-first-message.txt
  :language: text

.. note::

  I liked that on above message there were clear informations about:

  - Links to release notes, feedback and helping, contributing to Ubuntu, how to raise a bug and more.

Upgrade process - Issues
------------------------

And as expected ... first error appeared.

First error - not enough free space
+++++++++++++++++++++++++++++++++++

As expected :). After confirming the upgrade process (by pressing ``Y``) I got the following error:

.. error::

  .. literalinclude:: _static/snippets/upgrade-kubuntu-23.10-to-24.04-error-not-enough-space.txt
    :language: text


Checking free space
+++++++++++++++++++

First step was to check what is taking up space on my root partition.
This can be done with the following command:

.. code-block:: bash

    # Show disk usage of the root partition
    ncdu -x /

This command will show the disk usage of the root partition in nice and interactive way.

In command above:

- ``-x`` - is used to exclude other filesystems. This is important as I have separate partitions for major folders.

What was a suprise for me that the ``/var/lib/snapd/`` folder was using more than ``5GB (5.1GB)`` of space.

.. hint::

  - Snap is a software deployment and package management system for Linux.
    It allows you to install and manage applications in a sandboxed environment called a snap.
  - Snap packages are self-contained and work across a range of Linux distributions.
    They are easy to install, secure, and up-to-date.
  - Snap packages are stored in the ``/var/lib/snapd/`` folder (Default location).
  - More details about snap can be found in the :ref:`upgrade-kubuntu-23.10-to-24.04-resources` section.

.. note::

  - I belive that ``snap`` is a great tool, however it is consuming so much space.
  - And not sure why it is not using ``/usr/local`` or ``/opt`` partition only ``/var/lib``.


Increasing free space - moving snap folder
++++++++++++++++++++++++++++++++++++++++++

Investigation showed that from my ``20GB`` root partition, the ``/var/lib/snapd/`` folder was taking more than ``5GB`` of space,
which is ``25%`` of the total space. This was a lot of space for me.

.. code-block:: text

  5,1G    /var/lib/snapd/

More suprising was that I am not using snap that much. I have only few applications installed via snap.

.. literalinclude:: _static/snippets/upgrade-kubuntu-23.10-to-24.04-snap-list.txt
  :language: text

Finding partition with free space
+++++++++++++++++++++++++++++++++

Lucky for me I got free space on another partition - however this required preparation and moving files to another partition.

.. code-block:: text

  Filesystem                          Size  Used Avail Use% Mounted on
  /dev/mapper/vg_data-lv_data         331G  270G   45G  86% /mnt/myworkspace

.. important::

  - I had to move the ``/var/lib/snapd/`` folder to another partition.
  - I had to be sure to do that properly, as snap is used by GUI applications (for example ``Firefox``).

Creating initial plan for moving snap folder
++++++++++++++++++++++++++++++++++++++++++++

Initially I was thinking that this needs to be done from terminal (no GUI), so that was a plan.

- Find documents how to move snap folder to another partition (including stopping services).
  Save this in text file - as working on terminal without GUI has some limitations (like using ``Links`` as a web browser).
- Install terminal web browser (like ``Links``) - to have option to search internet.
- Go to terminal run-level - without GUI
- Stop snap services and unmount snap folders
- Move snap folder to another partition
- Run upgrade process again
- Check if everything is working fine after upgrade
- After distro upgrade - reboot is recommended

Second error - no WIFI in terminal
++++++++++++++++++++++++++++++++++

After collecting enough documents and installing required software, I was ready to start the process.

1. I've switched to terminal (without GUI) - run-level 3.

.. code-block:: bash

  # Check current run-level
  $ who -r
  # >> run-level 5

  # Switch to run-level 3
  sudo systemctl isolate multi-user.target

  # ...
  # When got console - I've login with my account
  who -r
  # >> run-level 3

2. Tried to check whether connection with Internet works (good practice from my old days as sysadmin)

I wanted be sure that working with ``Links`` is possible, so I've tried to open some website by running ``links``, and ...

.. error::

  - Got message that ``links`` is not able to open website


- I've checked others commands ``curl``, ``wget``, ``dig`` and all of them were not working.
- Suprised - **no WIFI in terminal** !!

.. important::

  - That was really suprise for me - I was not able to use Internet easily in terminal.
  - On my old days as sysadmin ``WIFI`` (networking) was runing on ``multi-user`` mode (run-level 3) and not on GUI.

.. tip::

  ``multi-user.target`` - This is a systemd target that sets up a non-graphical multi-user environment.
  It is similar to runlevel 3 in SysV init systems, where the system operates in a multi-user mode with
  networking but without a graphical interface.

  - Above information comes from ``Chat GPT`` when asked about ``multi-user.target``.

That was too much errors for me - had no time to try setup ``WIFI`` on console.
I've decided to move ``/var/lib/snapd/`` folder from GUI (with WIFI working).

.. code-block:: bash

  # Switch back to GUI
  sudo systemctl isolate graphical.target

Adjust plan - moving snap folder from GUI
+++++++++++++++++++++++++++++++++++++++++

After logging back into the GUI, I've created new plan:

- Stop snap services and unmount snap folders
- Move snap folder to another partition
- Run upgrade process again
- After distro upgrade - reboot is recommended
- Check if everything is working fine after upgrade and reboot


Moving snap folder - in GUI
+++++++++++++++++++++++++++

.. note::

  - I have hope that one day I will write some tutorial about safe process of moving snap folder to another partition.
  - For this post I will describe only steps which I've done which worked for me.
  - I was not familiar with snap configuration, however I trusted my experience and knowledge that I can manage this ...
    *(Dealing with advance configuration for Linux filesystem, partitions and folders
    was something which I was done a lot in past)*

So I've started with following steps:

1. Close all GUI applications (like ``Firefox``) which has been installed via snap (command ``snap list`` can help).
2. Leave open only console
3. Stop snap services

.. code-block:: bash

  sudo systemctl stop snapd
  sudo systemctl stop snapd.socket

4. Unmount snap folders

.. code-block:: bash

  for mount in $(mount | grep /snap | awk '{print $3}'); do
      sudo umount $mount
  done

5. Stop snapd-ns.mount

.. code-block:: bash

  sudo systemctl stop run-snapd-ns.mount

6. Verify that snap folders are unmounted

.. code-block:: bash

  mount | grep snap
  # Should not return anything

7. Create folder on another partition

.. code-block:: bash

  # Create folder on another partition
  sudo mkdir -vp /mnt/myworkspace/system-mounts-temporary/var-lib-snapd

8. Copy snap folder to another partition

- Below command will make sure to preserve all attributes of files and directories.

.. code-block:: bash

  # Rsync - copy files from one location to another
  rsync -aAX --info=progress2 /var/lib/snapd/ /mnt/myworkspace/system-mounts-temporary/var-lib-snapd/

  # Force sync (dump data to disks) - to be sure that everything is copied
  sync

9. Temporary rename snap folder

- Following steps allows revert changes if something goes wrong.

.. code-block:: bash

  # Rename old snap folder (Moving to another partition)
  sudo mv -v /var/lib/snapd/ /mnt/myworkspace/system-mounts-temporary/var-lib-snapd-old

  # Create new snap folder
  sudo mkdir -vp /var/lib/snapd/

10. Add new entry to ``/etc/fstab``

.. code-block:: text

  # 2024-07-28 - Moved /var/lib/snapd to /mnt/myworkspace/system-mounts-temporary/var-lib-snapd
  /mnt/myworkspace/system-mounts-temporary/var-lib-snapd  /var/lib/snapd  none    auto,bind       0       2

- Above entry will make sure that snap folder will be mounted with ``bind`` option.

11. Mount snap folder

.. code-block:: bash

  # Make sure that sytem is aware of new entry in /etc/fstab
  sudo systemctl daemon-reload

  # Mount snap folder
  sudo mount /var/lib/snapd/

12. Start snapd services

.. warning::

  - I've tried to run following commands - however this failed with errors during mount.
  - Not sure why - didn't try to investigate this.

  .. code-block:: bash

    sudo systemctl start snapd
    sudo systemctl start snapd.socket

13. Reboot system

- So I've decided to reboot the system. And was wondering whether my system will boot and run...

Upgrade process - final steps
-----------------------------

After rebooting the system, everything was working fine for me:

- Linux started
- GUI started
- Snap services started and were working fine
- Snap applications were working fine

Re-runnig upgrade process

.. code-block:: bash

  # Start the upgrade process
  sudo do-release-upgrade

.. note::

  - This time upgrade process started without any issues.
  - I've been informed that upgrade can take some time to finish

And after some time, the upgrade process was completed successfully.
*(This took around 2 hours on my laptop)*

So now.. that was the most scary part - rebooting the system after upgrade (no easy rollback)


System upgraded - welcome to Kubuntu 24.04
------------------------------------------

Lucky for me - after rebooting the system, everything was working fine. :)

And following is result from the ``neofetch`` command:

.. literalinclude:: _static/snippets/upgrade-kubuntu-23.10-to-24.04-neofetch02.txt
  :language: text

Removal of old snapd data
-------------------------

Once system was up and running, I've decided to remove old snapd data, no longer needed as snap was working with new location.

.. code-block:: bash

  # Remove old snapd data
  sudo rm -Rf /mnt/myworkspace/system-mounts-temporary/var-lib-snapd-old


Noticable issues after upgrade
------------------------------

Mostly everything was working fine and I started working on my laptop as usual.
However following are minor issues which I've noticed:

- Python ``venv`` stopped working

  - In some projects I needed to recreate python virutal environments (venv)

    - they stopped working
    - re-sourcing venv ``source venv/bin/activate`` - not worked

- Running ``Emacs`` fist time after upgrade

  - ``Emacs`` started consuming a lot of CPU
  - That was related with recompliation of packages during first run
  - This was resolved after above task was completed

Summary
-------

In this post, I've described the steps I took to upgrade my laptop from ``Kubuntu 23.10`` to ``Kubuntu 24.04``.
There were some challenges along the way, but I was able to overcome them and complete the upgrade successfully.

I've learned:

- Linux (``Kubuntu`` in this case) changed a lot in last years comparing with my past experience.
- Snap is a great tool, but it can consume a lot of space.
- Snap design doesn't work with ``symlinks`` to another partition - mount with ``bind`` worked for me.

I have really hope that this post helped you during the upgrade process of your ``Kubuntu`` system.

.. _upgrade-kubuntu-23.10-to-24.04-resources:

Resources
---------

Ubuntu / Kubuntu
++++++++++++++++

Following links are related with the upgrade process to ``Kubuntu 24.04``:

- `Ubuntu.com - Kubuntu Release Notes <https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes/Kubuntu>`_
- `Ubuntu.com - Kubuntu Upgrade Instructions <https://help.ubuntu.com/community/NobleUpgrades/Kubuntu>`_
- `Linuxconfig.org - Step-by-Step Howto Guide <https://linuxconfig.org/ubuntu-upgrade-to-24-04-noble-numbat-a-step-by-step-howto-guide>`_

Others
++++++

- `Snap - docs <https://snapcraft.io/docs>`_
- `Askubuntu.com - How to deal with snap using a lot of storage space <https://askubuntu.com/questions/1335229/how-to-deal-with-snap-using-a-lot-of-storage-space>`_
  *(Comments on this says - that 20GB is not enough when SNAP is used)*

