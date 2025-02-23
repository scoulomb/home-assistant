# QNAP extension setup

https://www.qnap.com/fr-fr/download?model=tr-002&category=documents

## Software control 

Via software CTRL we can JBOD, RAID0, RAID1 and RAID5+RAID 10 greyed. Individual not available. <!-- confirmed -->

RAID5+RAID 10 greyed as not compatible with unit TR002


### NAS Storage

Manual p 27

#### Pool + Thin or Thick volume

##### Create Pool + Thin or Thick volume


To configure
- 1. Configure software control on NAS
- 2. External Storage > configure raid group > Raid 0 > Create Poool to select as next action [via softawre ctrl we can do/select here JBDD, RAID0, RAID1
- 3. Storage/snapshot > create > newpool (or pop up due to selected next action in step 2)  > single (mode is single but in reality a raid0 group created in step 2) [menu done in case raid group not created previously?]
  - The raid group creation menu could have also been accessible via newpool
- 4. At this stage we have no external storage as it becomes a pool visible in storage snapshot
  - Also warn message saying it work only on NAS devices
- 5. Then Storage/snapshot > create volume on newly created pool (Thin or Thick volume)
  - Traditional config (volume) will not work as not created on pool but on raid group directly

##### Fallback Pool + Thin or Thick volume


To fallback
1. remove volime
2. storage/sanpshot > remove pool 
  - can see device in external storage
3. Storage snapshot > remove raid group
  - can see device in external storage not as a group

#### Traditionnal config volume

##### Create Traditionnal config volume

Repeat some steps from [create Thin or Thick volume](#create-pool--thin-or-thick-volume)


1. repeat 1
We can see raidgroup in external storage,it will disappear when volunme created
2. repeat 2 (can select next step as: create volune)
5. storage/snapsgot > create volume (or pop up due to selected next action)> and select traditionnal configuration volume

##### Fallbac kTraditionnal config volume

Same as [Fallback Pool + Thin or Thick volume](#fallback-pool--thin-or-thick-volume) except no pool to remove (step 2)
As no pool required


### External storage

Manual p 27

#### Create external storage 

Like nay standard HDD from NAS point of view

Repeat some steps from [create Thin or Thick volume](#create-pool--thin-or-thick-volume)


1. repeat 1
We can see raidgroup in external storage
2. repeat 2 (can select next step as: create external storage)
5. Externak storage > Format (under action) or pop up due to selected next action

##### Fallback External storage

Same as [Fallback Pool + Thin or Thick volume](#fallback-pool--thin-or-thick-volume) except no pool to remove (step 2) and no volume (step 1)



==> and we now undertand when we insert device proposal for NAS stroage or extenral storage

## Manual QNAP 


We can do exactly same config by setting jumper from SOFTWARE CTRL to JBOD, RAID-0, RAID-1 or indiviudal
Only difference us that we do not have to setup a raid group.
Otherwise can create voluime or external storage.
And individual mode is available unlike with software control (when create raid group uing oftware control we have [JBOD, RAID0, RAID1 and RAID5+RAID 10 greyed](#software-control) )
Also note we can not have a NAS extension with individual from table: https://www.qnap.com/fr-fr/product/tr-002#
Table hard to read as mixing manual raid mode and those same mode with softare control

<!-- animation individual software control does not mean we can have idividual via software control btw -->

Linux does not support SOFTWARE CONTROL (not clear if it is the setup via their software only or also the usage) from same table : https://www.qnap.com/fr-fr/product/tr-002# - will not test 


## Final setup and SUMMARY

- Manual RAID-0
- External storage 

So 
- set jumper to RAID-0 (fpr full reset [below](#reset-proc)) (if proc not applie correctly we may have a RAID mismatch)
- External storage > Format with EXT 4 (not exFAT as not supported by ms120:FAT32, NTFS, EXT 2/3/4, https://www.atoll-electronique.com/wp-content/uploads/2024/06/Mode-demploi-MS120.pdf)  (and we should have a volume of ~ 4 TO as we have 2 disk of 2TO in RAID-0) 
- We can see drive in QFILE

We can reformat if required, see [HBS implications with reformat](hbs.md#hbs-implications-with-reformat)

## Reset proc

Apply procedure here: https://www.qnap.com/s3/qutube/slides/ENsC1k2YR3E.p

1. In any mode other
than the
“Individual” mode
(Factory default is
Software Control)
Change the dip
switch mode to
the “Individual”
mode (all off)
2, Press ‘n hold the “SET”
button for 3 seconds
until a beep to switch
the mode to individual
(reset)*
*All data on drive(s) will be
erased
3, 
Change the dip
switch mode to
any other mode
Press and hold the
“SET” button for 3
seconds until a
beep to switch the
mode (2 only on for RAID0)
4. All data on drive(s)
will be erased


## Notes

Note: in storage snaphsot we have
- LUN similar to volume on pool (so thin or tick, not traditional), we can create LUN on pool
- VJBOD same to JBOD (all idsk seen as single drive) but using a remte NAS

<!-- OK CLEAR TR setup ccl -->
 -<!--no datamdel to do suffit -->



<!--ccl OK, + "We can reformat" OK-->

Then setup [HBS](hbs.md)

<!-- ccl ok -->


<!--ok -->

## Opt todo

- I could read music on ms120 OK
- (expect same on PI4)
- Less bandwidth on network as no DLNA reused for multiroom
    - test hdd to ms120 to avr to heos 150 over wifi => no improvements 
    - test hdd to pi4 via pizero moode over wifi 
    - Do we have less latency 
- m3u playlist
- copy to lacie