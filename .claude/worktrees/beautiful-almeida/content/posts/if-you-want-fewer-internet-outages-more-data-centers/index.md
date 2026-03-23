---
title: "If you want fewer Internet outages, more data centers!"
date: 2025-10-21
categories: 
  - "consumer-choice-center"
tags: 
  - "ai"
  - "data-centers"
coverImage: "data-centers.jpeg"
---

## **The US-east-1 outage of October 20th, 2025 explains why we need yet more data centers and energy capacity.**

Yesterday, Internet users in the US and abroad awoke to some kind of errors and issues when loading their favorite websites and services. A global outage! 

Hundreds of thousands of users flocked to real time monitoring websites like [Downdetector](https://downdetector.com/) to see why apps weren't loading, email was delayed, and why even some credit card payments weren't processed.

Within a few hours, the problem was localized to Amazon Web Service's **US-East-1**, a cluster of data centers and services mostly housed in and around Ashburn, Virginia, also known as "data center alley".

The us-east-1 region of AWS cloud services is one of the oldest and most reliant, well-connected via high-speed fiber to most data centers on the East Coast and offering an affordable cloud experience for cloud customers.

The precise cause will be investigated, but at least one remedy stands clear: we need to be building even more data centers and generating more energy so that fewer of these outages happen again.

**DNS will be the downfall of us all**

As any sysadmin or amateur web operator has had the unfortunate circumstance of learning themselves, the reported issue largely originated with DNS.

“At 12:26 AM on October 20, we identified the trigger of the event as DNS resolution issues for the regional DynamoDB service endpoints,” [wrote](https://health.aws.amazon.com/health/status) the AWS team on their status website.

Popular computing YouTuber and tech journalist Jeff Geerling was [quick](https://x.com/geerlingguy/status/1980455121495720224) to offer his “It was DNS!” t-shirts, owing to the [popular meme](https://itwasdns.net/) of IT technicians and engineers who are often ensnarled by the Internet's IP and domain naming system.

A handful of the [largest](https://techdator.net/aws-outage-disrupts-global-services-alexa-to-fortnite/) online websites and services were relying on AWS’ us-east-1 for their own servers, microservices architecture, or integrated features.

This is only natural, considering AWS offers some of the most competitive pricing and the company provides [nearly 30%](https://techcrunch.com/2025/10/20/amazon-dns-outage-breaks-much-of-the-internet/) of the global cloud computing market. I run a few AWS servers for small projects and backups as a failsafe for the servers I have at home.

Though it took a few hours to resolve, it’s clear the outage had a big impact on businesses, schools, and those who rely on the Internet for virtually everything they do.

The lucky ones were those who may have used a competitor – think Azure, Google cloud, Hetzner, or any other of the dozens of cloud computing providers who host their data themselves at their own facilities, like Twitter/X, Meta, or even parts of OpenAI’s ChatGPT. 

Just yesterday, Danish tech CEO DHH even [deleted](https://x.com/dhh/status/1980406035543388259) his company’s AWS accounts while on stage at a company meeting, demonstrating their own move to their own hosted cloud.

**The cloud trade-off has always been there**

The DNS snafu that brought down us-east-1 for a few hours revealed what many tech operators have already had to learn themselves: that running and operating digital services for global customers comes with significant trade-offs on cost and reliability.

Running data centers yourself is expensive, capital intensive, and requires constant vigilance. You must power them, staff them, and have emergency technicians on hand in case anything goes wrong. On the other hand, when something does go haywire, you can fix it yourself, rather than waiting for your service provider to fix it.

The opposite side is that cloud computing in today’s market is rather cheap, flexible, and usually, most of the time, has 100% uptime with no issues. It’s precisely why AWS is so popular and will remain so for a long time.

Relying on an outside vendor or service to offer your products and services to consumers is just part of the business calculation. Vulnerabilities must be compared along with cost, time, and effort. 

For massive companies that require 100% uptime they can fully control and tune, it’s clear why OpenAI and Meta have their own suite of decentralized servers. It’s to their advantage. The same could be said for privacy-oriented services or those with clients in more vulnerable sectors like healthcare and the military.

But for mom-and-pop websites or businesses that would rather spend more money elsewhere, cloud computing makes sense. This is especially true if you consider the dozens of widgets, scripts, and processes that make up microservices architecture that are the backbone of most digital apps and websites (this is worth a study on its own).

And even more so when you understand that most cloud computing companies have various regions and decentralized data center clusters around the country and the world to deliver their data to customers. They price that in.

**What this outage reveals**

When the first servers began to fail, the popular encrypted messenger app Signal began to have issues, allowing Elon Musk to [pitch](https://www.livemint.com/technology/tech-news/elon-musk-mocks-aws-outage-promotes-x-chat-as-most-major-apps-go-down-11760971820390.html) his new encrypted messages on the X app, which remained unaffected thanks to X’s [large data clusters](https://www.datacenterdynamics.com/en/news/elon-musks-x-suffers-another-major-outage/) in Portland, Sacramento, and Atlanta. But those data centers have had issues in the past. 

The usual suspects of the Senate Luddite caucus, however, were quick to inject their own agenda as to why this outage reveals that “Big Tech” must be broken up:

https://twitter.com/SenWarren/status/1980397661955191261

What if, rather than extrapolate the trade-off for businesses and individuals when it comes to cloud computing, and invite even more injurious solutions via antitrust or legislation, we just increase supply?

If we want to avoid Internet outages, we’re going to need more data centers.

Hyperscale data centers are [all the rage](https://netchoice.org/building-american-data-centers-to-meet-consumer-demand-create-new-tech-jobs-and-beat-china-on-ai/) in our country because they’re in _high_ demand. AI, self-driving cars, more connected services, and demand for data is pumping the building and construction of these data centers in hotspots around the country.

Boston Consulting Group estimates that nearly [$1.8 trillion](https://www.bcg.com/publications/2025/breaking-barriers-data-center-growth) in capital will be deployed in order to build data centers in just the next 5 years, answering the call of consumers who are actively wanting more technological innovations at the ready.

And if the US really does want to be competitive against China, and wants to host the next-generation innovations, we will need the energy capacity and computing power to do so. Our institutions and politicians should recognize that rather than try to win some ideological points.

And with the need for more data centers will naturally come the need for more energy production and capacity, and good public policy to incentivize this without red tape and the endless fear of [pointless liability litigation](https://consumerchoicecenter.org/energy-production-liability-protection/) that thwarts it.

Granted, there will be a lot of issues with how this grows in local communities. Backlash [against](https://www.washingtonpost.com/nation/2025/10/13/data-center-bans-lawsuit/) data center construction projects are now becoming a popular cry on the populist left and right. [False data](https://x.com/AndyMasley/status/1980317316165324942) on water usage and electricity hikes will be weaponized to oppose such needed projects.

In each case, tech and consumer advocates will have to be armed with the facts and the proper arguments for why we need America to play a part in the tech revolution, beginning with new data centers and energy abundance.

If we want 100% uptime of the important services and websites we need to function, that means doubling down on what powers them: smart energy policies to build out capacity and data centers to host and process that data. This is our wake-up call.

_Yaël Ossowski is deputy director at the Consumer Choice Center._
