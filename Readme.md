# CHEF-KOCH's Filter List [![Build Status](https://travis-ci.org/CHEF-KOCH/CKs-FilterList.svg?branch=master)](https://travis-ci.org/CHEF-KOCH/CKs-FilterList)

I created this project 2018 because I don't like the current well-known filter lists and I think they're often outdated and _incomplete_ or simply inefficient. My list is not restricted by any region. However, my personal focus is english, russian and swiss and germany regions since I speak these languages. 

The overall project goal is to block ads and reduce the traffic coming from the domains/websites you visit. The term 'ads' is not defined in this project because I also block cosmetically banners and popup stuff which I think only causes useless traffic without any real benefit.

<p align="center">
  <img width="480" height="430" src="https://i.imgur.com/rlEFwae.png">
</p>

[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/fold_left.svg?style=social&label=Follow%20%40CHEF-KOCH)](https://twitter.com/FZeven)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/CHEF-KOCH)
[![Discord](https://img.shields.io/discord/418256415874875402.svg?colorA=7289da&colorB=99aab5&label=Discord&logo=discord&maxAge=60)](https://discord.me/CHEF-KOCH)
[![Tip Me via PayPal](https://img.shields.io/badge/PayPal-tip%20me-green.svg?logo=paypal)](https://www.paypal.me/nvinside)


## Information about filter usage

**Site-specific or filter-based extensions such as AdBlock Plus, Request Policy, Ghostery, Priv3 and Sharemenot are in general to be avoided**. According to my own security expertise and history I can guarantee that these extensions do not add any real privacy layer to the Browser by itself - a proper implementation of the privacy requirements and development efforts on the Browser directly should be preferred on general solutions that prevent tracking by all third parties, rather than a list of specific URLs or hosts.

[I do not recommend using any filter lists](https://github.com/CHEF-KOCH/CKs-FilterList/wiki/Information-about-filter-usage), instead I highly recommend to work with whitelist only which are based on your own needs. However, a filter lists can help to reduce a possible attack surface based on the daily browsing habits.

## Project Structure

* `/CK's-Android-FilterList.txt` the main filter lists for your Ad-Blocker. The filter gets updated at least every 3 days.
* `/Android` includes the Android related filter list.
* `/HOSTS` contains HOSTS files for the project. The lists aren't updated frequently. 
* `/I2P & Onion` includes the I2P and .Onion related filter list `CK's-Onion-FilterList`.
* `/Malware` includes the anti-Malware related filter list `CK's-Malware-FilterList`.
* `/Not blocked` includes the excluded filter list `CK's-Wontblock-FilterList`.
* `/Test` includes multiple test filters for IP/ASN and uBlock + uMatrix rulesets.
* `CONTRIBUTING.md` is the file which shows you how to contribute to the project. It's essentially that you read the guidelines before you submit something.
* `Readme.md` is this file and is the general project overview file.
* `ToDo.md` is like the name already suggest the current todo list - same as the CONTRIBUTING.md it [needs to be read](https://github.com/CHEF-KOCH/CKs-FilterList/wiki/Filter-Policy-&-Issue-Tickets) before you submit something. 



## Supported Ad-Blockers

Make sure you have an ad-blocker installed in your desktop or mobile browsers that uses [Adblock Plus](https://adblockplus.org/) filter syntax:
* ![AdAway](https://i.imgur.com/AdWsIxw.png) [AdAway](https://github.com/AdAway/AdAway) - for **Android** only (partial supported)
* ![Blackada](https://i.imgur.com/XB1l9aG.png?1) [Blockada](http://blokada.org/) - for **Android** only
* ![DNS66](https://github.com/julian-klode/dns66) - for **Android** only
* ![uBock Origin](https://i.imgur.com/PSFuzKb.png) [uBlock Origin](https://github.com/gorhill/uBlock) or [Nano Adblocker](https://github.com/NanoAdblocker/NanoCore) - for **Browsers** as extension only
* ![AdGuard Browser Extension](https://i.imgur.com/zmMHq2j.png) [AdGuard](https://adguard.com/en/adguard-browser-extension/overview.html) - for **All Platforms** 
* ![pfSense](https://i.imgur.com/ElyO5Ie.png) [pfSense](https://www.pfsense.org/) with [pfBlockerNG](https://www.tecmint.com/install-configure-pfblockerng-dns-black-listing-in-pfsense/)
* ![Pi-hole](https://i.imgur.com/0mgKKma.png) [Pi-hole](https://pi-hole.net) - for **PI devices** 


## Partial supported 

The following blockers aren't fully supported, so they might work but they have some limitations and I personally can't recommend them. A more detailed explanation is given [here](https://github.com/CHEF-KOCH/CKs-FilterList/wiki/Limited-support-for-AdBlock-&-AdBlock-Plus).


* ![AdBlock](https://i.imgur.com/3KbyifF.png) [AdBlock](https://getadblock.com) - for **All Platforms** 
* ![AdBlock Plus](https://i.imgur.com/kPRCfhu.png) [Adblock Plus](https://adblockplus.org/) - for **Browsers** as extension only
* <img src="https://1blocker.com/img/icon.png" width=16> [1Blocker](https://1blocker.com) for **iOS or MacOS** devices only
* ![AdBlock Browser](https://i.imgur.com/6pkmjA0.png) [Adblock Browser](https://adblockbrowser.org/) - for **Android** and **iOS** devices only
* ![Brave Browser](https://user-images.githubusercontent.com/831718/32730079-e80c013c-c853-11e7-83b4-7443bc489581.png) [Brave Browser](https://www.brave.com) - (partial supported, request to add the list send)
* ![Opera Browser](https://i.imgur.com/bP0t9xc.png) [Opera Browser](https://www.opera.com) - (partial supported, request to add the list send)


## CHEF-KOCH's FilterList

[CHEF-KOCH's FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/CK's-FilterList.txt&title=CHEF-KOCH's-Filter-List) - Click on the link in order to sub the filter list via your Browser.



## Documentation

For a more detailed project description and documentation please see the [Wiki pages](https://github.com/CHEF-KOCH/CKs-FilterList/wiki).



## Optional lists

The following filters might not getting into the main filter list (_CK's-FilterList.txt_) and are labeled as [optional](https://github.com/CHEF-KOCH/CKs-FilterList#optional-lists), there also not getting as fast updates, their update interval is set to 14 days. 



### uBlock, 1Block, etc optional filter lists.

Filter Name | Description | Sub link
--- | --- | ---
Ad & Tracker Filter List | Blocks additional Ads & Trackers | [CHEF-KOCH's Ad & Tracker Filter List](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Ad%20%26%20Tracker/CK's-Ad-Tracker-FilterList.txt&title=CHEF-KOCH's-Ad-&-Trackers-Filter-List)
Android | Blocks ads & trackers and other unneeded Android traffic | [CHEF-KOCH's Android FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Android/CK's-Android-FilterList.txt&title=CHEF-KOCH's-Android-Filter-List)
Cooperation: Adobe | Blocks all Adobe traffic | [CHEF-KOCH's Adobe FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Corporations/Adobe/CK's-Adobe-FilterList.txt&title=CHEF-KOCH's-Adobe-Filter-List)
Cooperation: Apple | Blocks all Apple traffic | [CHEF-KOCH's Apple FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Corporations/Apple/CK's-Apple-FilterList.txt&title=CHEF-KOCH's-Apple-Filter-List)
Cooperation: Avast/CCleaner | Blocks all Avast/CCleaner traffic | [CHEF-KOCH's Avast/CCleaner FilterList](https://subscribe.adblockplus.org/?location=https://github.com/CHEF-KOCH/CKs-FilterList/blob/master/Corporations/CCleaner/CK's-CCleaner-FilterList.txt&title=CHEF-KOCH's-CCleaner-Filter-List)
Cooperation: Cloudflare | Blocks all Cloudflare traffic | [CHEF-KOCH's Cloudflare FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Corporations/Cloudflare/CK's-Cloudflare-FilterList.txt&title=CHEF-KOCH's-Cloudflare-Filter-List)
Cooperation: Facebook | Blocks all Facebook & services traffic | [CHEF-KOCH's Facebook FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Corporations/Facebook/CK's-Facebook-FilterList.txt&title=CHEF-KOCH's-Facebook-Filter-List)
Cooperation: Google | Blocks all Google & services traffic | [CHEF-KOCH's Google FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Corporations/Google/CK's-Google-FilterList.txt&title=CHEF-KOCH's-Google-Filter-List)
Cooperation: Instagram | Blocks all Instagram & services traffic | [CHEF-KOCH's Instagram FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Corporations/Instagram/CK's-Instagram-FilterList.txt&title=CHEF-KOCH's-Instagram-Filter-List)
Cooperation: Microsoft | Blocks all Microsoft & services traffic | [CHEF-KOCH's Microsoft FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Corporations/Microsoft/CK's-Microsoft-FilterList.txt&title=CHEF-KOCH's-Microsoft-Filter-List)
Cooperation: Mozilla | Blocks all Mozilla & services traffic | [CHEF-KOCH's Mozilla FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Corporations/Mozilla/CK's-Mozilla-FilterList.txt&title=CHEF-KOCH's-Mozilla-Filter-List)
Cooperation: Pinterest | Blocks all Pinterest & services traffic | [CHEF-KOCH's Pinterest FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Corporations/Pinterest/CK's-Pinterest-FilterList.txt&title=CHEF-KOCH's-Pinterest-Filter-List)
App: Skype | Skype Ad-Free | [CHEF-KOCH's Skype Ad-Free FilterList](https://subscribe.adblockplus.org/?location=https://github.com/CHEF-KOCH/CKs-FilterList/blob/master/Corporations/Skype%20Ad-Free/CK's-Skype-FilterList.txt&title=CHEF-KOCH's-Skype-Ad-Free-Filter-List)
App: Spotify | Spotify Ad-Free | [CHEF-KOCH's Spotify Ad-Free FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Corporations/Spotify%20Ad-Free/CK's-Spotify-FilterList.txt&title=CHEF-KOCH's-Spotify-Ad-Free-Filter-List)
Fonts | Block all Fonts | [CHEF-KOCH's Fonts FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Fonts/CK's-Fonts-FilterList.txt&title=CHEF-KOCH's-Fonts-Filter-List)
I2P & Onion | Blocklist for bad I2P & Onion domains | [CHEF-KOCH's I2P & Onion FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/I2P%20%26%20Onion/CK's-Onion-FilterList.txt&title=CHEF-KOCH's-I2P-&-Onion-Filter-List)
Malware | Blocklist for Malware | [CHEF-KOCH's Malware FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Malware/CK's-Malware-FilterList.txt&title=CHEF-KOCH's-I2P-&-Onion-Filter-List)
Wontblock | Unblock the Internet and good pages | [CHEF-KOCH's Wontblock FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Not%20blocked/CK's-Wontblock-FilterList.txt&title=CHEF-KOCH's-I2P-&-Onion-Filter-List)
Torrent | Blocklist for bad Torrent Tracker | [CHEF-KOCH's Torrent FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Torrent/CK's-Torrent-FilterList.txt&title=CHEF-KOCH's-I2P-&-Onion-Filter-List)



### uMatrix & HOSTS only optional filter lists.


HOSTS and uMatrix only filter lists - please keep in mind that _there not sub-clickable_ (like the above uBO list). There will also be [no 127.0.0.1 versions](https://github.com/CHEF-KOCH/CKs-FilterList/wiki/127.0.0.1-vs-0.0.0.0). 


Filter Name | Description | Sub link
--- | --- | ---
Ad & Tracker Filter List | Blocks additional Ads & Trackers | [CHEF-KOCH's Ad & Tracker FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/HOSTS/CK's-Ad-Tracker-HOSTS-FilterList.txt&title=CHEF-KOCH's-Ad-&-Trackers-Filter-List)
Adguard | Blocks AdGuard related traffic | [CHEF-KOCH's Adguard FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/HOSTS/CK's-Adguard-HOSTS-FilterList.txt&title=CHEF-KOCH's-Adguard-Filter-List)
Cooperation: Adobe | Blocks all Adobe traffic | [CHEF-KOCH's Adobe FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/HOSTS/CK's-Adobe-HOSTS-FilterList.txt&title=CHEF-KOCH's-Adobe-Filter-List)
Cooperation: Apple | Blocks all Apple traffic | [CHEF-KOCH's Apple FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/HOSTS/CK's-Apple-HOSTS-FilterList.txt&title=CHEF-KOCH's-Apple-Filter-List)
Cooperation: Avast/CCleaner | Blocks all Avast/CCleaner traffic | [CHEF-KOCH's Avast/CCleaner FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/HOSTS/CK's-CCleaner-HOSTS-FilterList.txt&title=CHEF-KOCH's-CCleaner-Filter-List)
Cooperation: Cloudflare | Blocks all Cloudflare traffic | [CHEF-KOCH's Cloudflare FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/HOSTS/CK's-Cloudflare-HOSTS-FilterList.txt&title=CHEF-KOCH's-Cloudflare-Filter-List)
Cooperation: Facebook | Blocks all Facebook traffic | [CHEF-KOCH's Facebook FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/HOSTS/CK's-Facebook-HOSTS-FilterList.txt&title=CHEF-KOCH's-Facebook-Filter-List)
Cooperation: Google | Blocks all Google & services traffic | [CHEF-KOCH's Google FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/HOSTS/CK's-Google-HOSTS-FilterList.txt&title=CHEF-KOCH's-Google-Filter-List)
Cooperation: Instagram | Blocks all Instagram & services traffic | [CHEF-KOCH's Instagram FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/HOSTS/CK's-Instagram-HOSTS-FilterList.txt&title=CHEF-KOCH's-Instagram-Filter-List)
Cooperation: Microsoft | Blocks all Microsoft & services traffic | [CHEF-KOCH's Microsoft FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/HOSTS/CK's-Microsoft-HOSTS-FilterList.txt&title=CHEF-KOCH's-Microsoft-Filter-List)
Cooperation: Mozilla | Blocks all Mozilla & services traffic | [CHEF-KOCH's Mozilla FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/HOSTS/CK's-Mozilla-HOSTS-FilterList.txt&title=CHEF-KOCH's-Mozilla-Filter-List)
Cooperation: NSA,FBI,CIA | Blocks all NSA, CIA, FBI etc 'spying' server connections | [CHEF-KOCH's NSA FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/Corporations/NSABlocklist/CK's-NSABlocklist-FilterList.txt&title=CHEF-KOCH's-Mozilla-Filter-List)
Cooperation: Pinterest | Blocks all Pinterest & services traffic | [CHEF-KOCH's Pinterest FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/HOSTS/CK's-Pinterest-HOSTS-FilterList.txt&title=CHEF-KOCH's-Pinterest-Filter-List)
App: Skype | Skype Ad-Free | [CHEF-KOCH's Skype Ad-Free FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/HOSTS/CK's-Skype-HOSTS-FilterList.txt&title=CHEF-KOCH's-Skype-Ad-Free-Filter-List)
App: Spotify | Spotify Ad-Free | [CHEF-KOCH's Spotify Ad-Free FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/HOSTS/CK's-Spotify-HOSTS-FilterList.txt&title=CHEF-KOCH's-Spotify-Ad-Free-Filter-List)
uMatrix | uMatrix / HOSTS based lists (domains only from CK's-FilterList) | [CHEF-KOCH's uMatrix FilterList](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/CHEF-KOCH/CKs-FilterList/master/uMatrix/CK's-uMatrix-FilterList.txt&title=CHEF-KOCH's-Spotify-Ad-Free-Filter-List)


## Report issues, unblocked ads or trackers

You can report issue [here](https://github.com/CHEF-KOCH/CKs-FilterList/issues), keep in mind that this requires that you read the [contribution guidelines](https://github.com/CHEF-KOCH/CKs-FilterList/blob/master/CONTRIBUTING.md) first.  


#### Like the list? 

Star it on GitHub! :star: or consider making a [donation](https://github.com/CHEF-KOCH/Donations). :muscle:


## Credits 

:construction: The following people contributed to CK's Filter List in order to improve the project. :construction:
* The-Commissioner


## License

The project and it's content of CHEF-KOCH's Filter List is licensed under a [ISC License](https://github.com/CHEF-KOCH/CKs-FilterList/blob/master/LICENSE).
