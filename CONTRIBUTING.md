## Reporting Issues

You need to read and accept the following guidelines in order to report something: [Filter Policy & Issue Tickets](https://github.com/CHEF-KOCH/CKs-FilterList/wiki/Filter-Policy-&-Issue-Tickets).

**CHEF-KOCH's FilterList maintenance support policy:**

:white_check_mark: The list is **not limited** by English websites only.

:x: Porn websites. Maybe in the near future in an separate list.

:x: P2P (BitTorrent, etc.) and other copyright infringing, media sharing/streaming websites.

:white_check_mark: Anti-censorship pages.
 
:white_check_mark: Websites containing or related to illegal activity/content.

:arrow_right: Ensure you checked the [ToDo.md](https://github.com/CHEF-KOCH/CKs-FilterList/blob/master/ToDo.md) before you submit something.

:arrow_right: **[Report issues, unblocked ads or trackers.](https://github.com/CHEF-KOCH/CKs-FilterList/issues)**

###### Tips

:bulb: Before reporting any problem, make sure that it is in fact [CHEF-KOCH's FilterList](https://github.com/CHEF-KOCH/CKs-FilterList) that is causing the issue. Confirm this by temporarily disabling all other installed lists that you may have subscribed. Including the built in "Tracking Protection" - [or Ads](https://www.ctrl.blog/entry/chrome-adblocker) blocking mechanism.

:bulb: Remedy any issues yourself instantly by simply disabling your ad blocker for the affected website.

:bulb: Rules like `website.com##script:inject(abort-on-property-write.js, uabInject)` are invalid and the Pull Request gets rejected.

:bulb: Check yourself for redundant filter rules, read [here](https://github.com/CHEF-KOCH/CKs-FilterList/wiki/%5BHow-To%5D-Check-for-redundancies).


## Notes

:grey_exclamation: CHEF-KOCH's FilterList uses the Adblock/uBlock/AdGuard filter syntax and ideally should be used with uBlock, AdGuard etc. for the intended/optimal performance. However, the list can be used with other adblockers that support the filter syntax (these are limited supported due their inefficiency). 

:grey_exclamation: **Untick the "Allow Acceptable Ads" checkbox in Adblock Plus:**

:one: Click on the red "ABP" icon.

:two: Click on "Options".

:three: Untick the "Allow Acceptable Ads" checkbox.

:grey_exclamation: **Still seeing some unblocked ads while using CHEF-KOCH's FilterList?** This is because in some cases I can't have access to certain websites to create ad blocking filters due to those websites having regional/country specific restrictions or require a login account (webmail, social media, etc.).


###### How To's

* [[How To] Check for redundancies](https://github.com/CHEF-KOCH/CKs-FilterList/wiki/127.0.0.1-vs-0.0.0.0)
* [[How To] Compare or Remove duplicate entries](https://github.com/CHEF-KOCH/CKs-FilterList/wiki/%5BHow-To%5D-Check-for-redundancies)
* [[How To] Sort the filters](https://github.com/CHEF-KOCH/CKs-FilterList/wiki/%5BHow-To%5D-Compare-or-Remove-duplicate-entries) 


###### Recommended Links

:link: [Known Adblock Plus subscriptions](https://adblockplus.org/subscriptions) (For supplemental coverage, if required.)

:link: [Google Analytics Opt-out Browser Add-on](https://tools.google.com/dlpage/gaoptout) (Opt-out of Google Analytics.)

:link: How to [write correct filters](https://adblockplus.org/en/filters), the filters itself are explained over [here](https://adblockplus.org/en/filter-cheatsheet). uBO examples are given [here](https://github.com/gorhill/uBlock/wiki/Static-filter-syntax) and AdGuard Guide is available [here](https://kb.adguard.com/en/general/how-to-create-your-own-ad-filters).


###### You may use the following tools

- [Redundant Rule Checker](https://arestwo.org/famlam/redundantRuleChecker.html)
- [Adblock Syntax](https://adblockplus.org/filters)
- [Regex Visualizer](http://www.regexper.com/)
- [Filter syntax for HTML, CSS or JavaScript Useful links and resources](https://github.com/CHEF-KOCH/CKs-FilterList/wiki/Filter-syntax-for-HTML,-CSS-or-JavaScript---Useful-links-and-resources)