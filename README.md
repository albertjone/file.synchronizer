##

### definition
File synchronization (or syncing) in computing is the process of ensuring that computer files in two or more locations are updated via certain rules.

### types
  - one-way file synchronization
    updated files are copied from a source location to one or more target locations, but no files are copied back to the source location.

  - two-way file synchronization
    updated files are copied in both directions, usually with the purpose of keeping the two locations identical to each other

### features
  - one-way file synchronization
  - two-way file synchronization
  - real-time file sync
  - encryption
  - compressing
  - Conflict detection where a file has been modified on both sources, as opposed to where it has only been modified on one. Undetected conflicts can lead to overwriting copies of the file with the most recent version, causing data loss. For conflict detection, the synchronization software needs to keep a database of the synchronized files. Distributed conflict detection can be achieved by version vectors.
  - Open Files Support ensures data integrity when copying data or application files that are in-use or database files that are exclusively locked.
  - Specific support for using an intermediate storage device, such as a removable flash disc, to synchronize two machines. Most synchronizing programs can be used in this way, but providing specific support for this can reduce the amount of data stored on a device.
  - Specific support for using an intermediate storage device, such as a removable flash disc, to synchronize two machines. Most synchronizing programs can be used in this way, but providing specific support for this can reduce the amount of data stored on a device.
  - The ability to view differences in individual files.
  - Backup between operating systems and transfer between network computers.
  - have gui interfaces

### opensource competitions
  refer to https://en.wikipedia.org/wiki/Comparison_of_file_synchronization_software#Open-source
  below only show single language case:
  - python
    * Conduit
    * Seafile community edition
  - go
    * InterPlanetaryFileSystem
    * Syncthing
  - c
    * rsync
  - java
    * DirSync Pro
  - c#
    * SparkleShare
    * iFolder
    * OneSync
  - c++
    * Synkron
    * luckyBackup
    * FreeFileSync
