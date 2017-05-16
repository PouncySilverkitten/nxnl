# nxnl
A small CLI for interrogating snapshots generated by BotBot on euphoria.io.

## Commands

`-r`
Shows **r**ooms in order of highest botling occupancy.

`-lr /room/`
Prints a **l**ist of all botlings present in /**r**oom/.

`-l`
Provides a **l**ist of the names of all botlings in a snapshot.
`-d`
Prints a list of all botlings which are **d**uplicates - i.e. have more than one instance.

`-s @botname`
Shows **s**tats for a specific bot.

`-p`
Provides a list of all **p**aused botlings.

`-pr /room/`
Outputs a list of all **p**aused botlings in /**r**oom/.

## To Use
Add script to an unzipped screenshot directory, then run:
`python3 nxnl.py *command here*`
as required.
