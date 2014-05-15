tinypower
=========
This app is beta, so there could be some bugs.
If you find one, please create an issue.
And if I have enough time on my hands, I'll deal with it :)

Overview:

It handles acpi events, so custom actions can be assigned....can change screen timeout...indicates battery status..and throws notifications for certain events


tidybattery fork + acpi handling + dpms management

Installation:

Important!!!!!!!!!!
You have to set systemd button handling to ignore, otherwise the
custom actions for acpi events won't work correctly.
/etc/systemd/logind.conf
And there change it to:
HandlePowerKey=ignore
HandleSuspendKey=ignore
HandleHibernateKey=ignore
HandleLidSwitch=ignore

Features:

Low Power Autosuspend:

- Suspends when battery is below 5 percent


Notifications:

- If you change screenbrightness
- When you plug/unplug your charger


ACPI Handling:

The following events can have custom actions:

- Power Button Press
- Lid Close
- Suspend Button

You can assing a systemd action to the different events,
like PowerOff, Suspend, Hibernate, Nothing


DPMS Handling:

You can set the Screen-Off time for when on battery or when the charger
is plugged.


Battery-Icons from faenza/faience icon theme 
http://tiheum.deviantart.com/art/Faience-icon-theme-255099649
http://tiheum.deviantart.com/art/Faenza-Icons-173323228
