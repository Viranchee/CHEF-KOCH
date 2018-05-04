# CHEF-KOCH's Filter List

[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/fold_left.svg?style=social&label=Follow%20%40CHEF-KOCH)](https://twitter.com/CKsTechNews)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/CHEF-KOCH)
[![Discord](https://discordapp.com/api/guilds/418256415874875402/widget.png)](https://discord.me/CHEF-KOCH)


## Installation

Make sure you have an ad-blocker installed in your desktop or mobile browsers that uses [Adblock Plus](https://adblockplus.org/) filter syntax:
* ![AdBlock](https://i.imgur.com/3KbyifF.png) [AdBlock](https://getadblock.com)
* ![AdBlock Plus](https://i.imgur.com/kPRCfhu.png) [Adblock Plus](https://adblockplus.org/)
* ![uBock Origin](https://i.imgur.com/PSFuzKb.png) [uBlock Origin](https://github.com/gorhill/uBlock) or [Nano Adblocker](https://github.com/NanoAdblocker/NanoCore)
* ![AdGuard Browser Extension](https://i.imgur.com/zmMHq2j.png) [AdGuard Browser Extension](https://adguard.com/en/adguard-browser-extension/overview.html)
* ![AdBlock Browser](https://i.imgur.com/6pkmjA0.png) [Adblock Browser](https://adblockbrowser.org/) for **Android** and **iOS** devices
* ![Brave Browser](https://user-images.githubusercontent.com/831718/32730079-e80c013c-c853-11e7-83b4-7443bc489581.png) [Brave Browser](https://www.brave.com) (Included by default)
* ![Opera Browser](https://i.imgur.com/bP0t9xc.png) [Opera Browser](https://www.opera.com)
* <img src="https://1blocker.com/img/icon.png" width=16> [1Blocker](https://1blocker.com) for iOS or MacOS devices
* ![pfSense](https://i.imgur.com/ElyO5Ie.png) [pfSense](https://www.pfsense.org/) with [pfBlockerNG](https://www.tecmint.com/install-configure-pfblockerng-dns-black-listing-in-pfsense/)
* ![Pi-hole](https://i.imgur.com/0mgKKma.png) [Pi-hole](https://pi-hole.net)

### CK's Filter List todo

- [ ] Check redundant entries automatically (is that it even possible?) (high-prio)
- [ ] Remove most entries and replace it with more intelligent syntax rules which works for all websites (high-prio)
- [ ] Reduce the file-size (low-prio)
- [ ] Sort it alphabetically (low-prio)
- [ ] Make categories for Porn, Malware, etc. to easier work with the list (helps possible contributors) (high-prio)
- [ ] The checksum is incorrect because I make my changes (generate the checksum and then I need to paste it into the list which obviously changes the checksum again ... This needs to be changed (is that even possible?) (low-prio)
- [x] Readme.md improvements
- [ ] Fix all reported issue (high-prio)
- [ ] Maybe separate the list in his categories (low-prio)
- [ ] Maybe add an description like !Facebook before each entry (related to ^^)
- [ ] Create a uMatrix ruleset
- [x] Add an ISSUE_TEMPLATE

#### Why do you keep dead domains?

Due the following simple reason, once a domain is dead another 'bad' guy could kick-in and buy it in order to abuse it.

#### uBlock Origin / Nano Adblocker
  - Open uBlock Origin (uBo) options panel
  - Navigate to Filter lists page/tab
  - On the bottom of the page, there should be an 'Custom' section (you might need to click the + to reveal the 'Import' button, click on it:
  - Copy & paste into the textbox:
  
  ```
  https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/CK's-FilterList.txt
  ```
  
  - Now there should appear a yellow button called "Parse", click it
  - Lastly you need to go to the top and hit the yellow "Update now" button
  - This method works quite similar in order Browser Extensions too, like AdBlock Plus or AdGuard.


### [Subscribe to CHEF-KOCH's FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/CK's-FilterList.txt&title=CHEF-KOCH's-Filter-List)

## [Report issues, unblocked ads or trackers](./CONTRIBUTING.md)

#### Like my list? Star it on GitHub! :star: (Desktop site) or consider making a [donation](https://github.com/CHEF-KOCH/Donations). :muscle:

## License

Content of CHEF-KOCH's Filter List is licensed under a [GNU General Public License v3.0](https://github.com/CHEF-KOCH/CKs-FilterList/blob/master/LICENSE).
