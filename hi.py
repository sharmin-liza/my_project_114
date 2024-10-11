# Import the required module for text 
# to speech conversion
from gtts import gTTS
import os
mytext =("
HomeHome ProductsResource CenterThreatsWhat is a Trojan Horse Virus? Types and How to Remove it
What is a Trojan Horse Virus? Types and How to Remove it
Trojan Horse
When the horse's belly opened at night it was too late. The Greeks had finally succeeded in capturing the long besieged city of Troy, bringing the Trojan War to an end. Thousands of years later, the myth of the Trojan horse still lives on, albeit today in an unflattering connotation. For what once stood for a brilliant trick and a masterful feat of engineering is nowadays regarded as a malicious digital pest whose sole aim is to wreak havoc on its victims' computers unnoticed. It does this by reading passwords, recording keyboard strokes or opening the door for further malware that can even take the entire computer hostage. These actions can include:

Deleting data
Blocking data
Modifying data
Copying data
Disrupting the performance of computers or computer networks
Unlike computer viruses and worms, Trojans are not able to self-replicate.

Types of Trojan
Backdoor Trojans
They are one of the simplest but potentially most dangerous types of Trojan. This is because they can either load all sorts of malware onto your system in their role as a gateway, or at least ensure that your computer is vulnerable to attack. A backdoor is often used to set up botnets. Without your knowledge, your computer becomes part of a zombie network that is used for attacks. Furthermore, backdoors can allow code and commands to be executed on your device or monitor your web traffic.

Exploit
Exploits are programs that contain data or code that take advantage of a vulnerability within an application on your computer.

Rootkit
Rootkits are designed to conceal certain objects or activities in your system. Often their main purpose is to prevent malicious programs being detected, in order to extend the period in which the programs can run on an infected computer.

Dropper/downloader Trojans
One of the best-known dropper Trojans is the Emotet malware, which has now been rendered harmless but which, in contrast to a backdoor Trojan, cannot execute any code on the PC itself. Instead, it brings other malware with it, for example the banking Trojan Trickbot and the ransomware Ryuk. Droppers are therefore similar to downloader Trojans, the difference being that downloaders need a network resource to pull malware from the network. Droppers themselves already contain the other malicious components in the program package. Both types of Trojan can be remotely updated in secret by the programmers responsible, for example so that virus scanners cannot detect them with new definitions. New functions can also be added in this way.

Banking Trojans
Banking Trojans are among the most widespread Trojans. Given the increasing acceptance of online banking, as well as the carelessness of some users, this is no wonder – they are a promising method for attackers to get their hands on money quickly. Their goal is to obtain the access credentials to bank accounts. To do this they use phishing techniques, for example by sending the alleged victims to a manipulated page where they are supposed to enter their access credentials. Accordingly, when using online banking you should ensure that you use secure methods for verification, such as only the app of the respective bank, and never enter your access data on a web interface.

DDoS Trojans
Distributed denial-of-service (DDoS) attacks continue to haunt the web. In these attacks, a server or network is torpedoed with requests, usually by a botnet. In mid-June 2020, for example, Amazon fended off a record attack on its servers. For over three days, Amazon's web services were targeted with a data throughput of 2.3 terabytes per second. There must be an enormous botnet to achieve that kind of computing power. Botnets consist of zombie computers, so to speak. On the face of it they are running normally, but they are also functioning silently as attackers. The reason for this is a Trojan with a backdoor component that slumbers unnoticed on the computer and, if necessary, is activated by its operator. If a botnet attack or a DDoS attack is successful, websites or even entire networks are no longer accessible.

Fake antivirus Trojans
Fake antivirus Trojans are particularly insidious. Instead of protecting, they get every device into serious trouble. With alleged virus findings, they want to cause panic among unsuspecting users and persuade them to purchase effective protection by paying a fee. But instead of a helpful virus scanner, the user only gets more problems, as their payment data is conveyed to the Trojan originator for further misuse. So if you suddenly get a virus warning in your browser when visiting a website, you should ignore this and only trust your system virus scanner.

Trojan-GameThief
This type of program steals user account information from online gamers.

Trojan-IM (Instant Messaging)
Trojan-IM programs steal your login data and passwords for instant messaging programs such as ICQ, MSN Messenger, AOL Instant Messenger, Yahoo Pager, Skype, etc. One could argue that these messengers are barely in use nowadays. However, even new messenger services are not immune to Trojans. Facebook Messenger, WhatsApp, Telegram or Signal could also become targets of Trojans. As recently as December 2020, a Windows Trojan was commandeered via a Telegram channel. Instant messaging should also be protected against dangerous phishing attacks.

In January 2018, security researchers at Kaspersky discovered a Trojan called Skygofree. The malware has extremely advanced functions and can, for example, connect to Wi-Fi networks on its own, even if the user has deactivated the function on their device. The Skygofree Trojan can also monitor the popular messenger service WhatsApp. It reads messages and can also steal them.

Trojan-Ransom 
This type of Trojan can modify data on your computer so that your computer doesn’t run correctly or you can no longer use specific data. The criminal will only restore your computer’s performance or unblock your data after you have paid them the ransom money that they demand.

SMS Trojans
They may seem like a relic from another century, yet they are still active and pose a significant threat. SMS Trojans such as the Android malware Faketoken can work in different ways. Faketoken, for example, sends mass SMS messages to expensive international numbers and disguises itself in the system as a standard SMS app. The smartphone owner has to pay the costs for this. Other SMS Trojans establish connections to expensive premium SMS services.

Trojan-Spy
Trojan-Spy programs can spy on how you’re using your computer – for example, by tracking the data you enter via your keyboard, taking screenshots or getting a list of running applications.

Trojan-Mailfinder 
These programs can harvest email addresses from your computer.

In addition, there are other types of Trojans:

Trojan-ArcBomb
Trojan-Clicker
Trojan-Notifier
Trojan-Proxy
Trojan-PSW 
Trojans attack all devices and how to remove it
Trojans now not only target Windows computers, but also Mac computers and mobile devices. Accordingly, you should never feel too safe or be on the internet without up-to-date anti-malware protection such as Kaspersky Plus Internet Security. Malware often gets onto computers via infected attachments, manipulated text messages or bogus websites. However, there are also secret service Trojans that can be installed on the target systems remotely without the user noticing and without any interaction on the part of the targets.

The Pegasus software from the Israeli manufacturer NSO, for example, is distributed via the mobile phone network. Pegasus includes a powerful arsenal of interception options. The device can be read completely, calls can be recorded, or the phone can be used as a bugging device.

In Germany, too, police authorities use a state Trojan to monitor and track criminals. However, the malware, known in officialese as source TKÜ software, may not be used for surveillance without a court order.

So-called backdoors can be used to load malware onto a PC unnoticed

Cybercriminals want to cause maximum damage with Trojans
If surveillance software is used by the state to track and punish criminal offenses, cybercriminals have exactly the opposite in mind. In the latter case, it is all about personal enrichment at the expense of their victims. In doing so, the criminals use different programs, sometimes even entire malware chains. How do they do it? One example may be a backdoor installed unnoticed on the computer via an infected email attachment.

This gateway ensures that further malware is loaded onto the PC secretly and silently without being noticed. Another example is a keylogger to record keystrokes such as passwords or confidential content, a banking Trojan to steal financial data, or ransomware that encrypts the entire computer and only releases the hijacked data following payment of a significant amount of bitcoin. Notorious in this context is the malware Emotet, which periodically makes its rounds and is described as the "most destructive malware."

Strictly speaking, the "Trojan King" is a bot network that uses spam emails and infected Word or Excel documents to find its victims. The BSI has set up an extra page with information on Emotet. In summary:

Emotet is considered one of the most destructive and dangerous Trojans.
It isn't yet known who is behind Emotet.
The damage caused by Emotet runs into the millions.
Companies are the main targets. Private users can still be affected if Emotet reads the stored email addresses from address books and adds them to its immense database.
To contain the danger, in addition to having up-to-date software, macros should be deactivated in Word and Excel and no attachments should be opened from emails from unknown senders.
Piggybacking onto the end device
Trojans are not only found in email attachments. They can also "piggyback" on supposedly free programs. Once again, therefore, it is important not to use dubious sources for software downloads such as codec packs or cracked programs, even if you might save a few euros. The damage that can be caused by Trojans often exceeds the value of the software if it had been purchased through regular channels.

Incidentally, a Trojan should not be confused with a virus. Computer viruses reproduce independently, whereas a Trojan is merely a door opener – but with potentially devastating consequences.

Therefore, here is a checklist on how to protect yourself and your devices from Trojans:

Think before you open attachments from emails. Check the sender and the text, and consider whether the attachment really needs to be opened.
Always keep your mobile and stationary systems up to date. Install security updates on a regular basis, both for the operating system and the installed programs.
Do not allow macros in Word and Excel.
Do not click on links without thinking. There is also the possibility of a drive-by infection. This is an unnoticed installation of malware when visiting bogus websites, which ensure that the malware is downloaded onto the home system in the background.
Avoid downloading programs from unsafe sources. On mobile devices, avoid installing apps that are not offered in the Google Play Store or the Apple Store.
Always display all file extensions. This will tell you if a supposed image – usually with a jpg extension – is backed by an executable file with an exe extension.
As an additional security measure, use two-factor authentication via a mobile app and strong passwords, or ideally a password manager.
Always scan your system with a virus scanner with up-to-date definitions. The Kaspersky Internet Security suite protects you from malicious programs and malicious content.
Make regular backups of your data. Not only on cloud services, but also on a physical data carrier, such as a mobile SSD or HDD hard drive with a USB connection.
Be careful when surfing the web
The Trojans mentioned here are the best-known types. What they all have in common is that they can only get onto the end device with the help of the user. However, if you surf the web carefully, do not open email attachments without thinking, and only obtain programs from secure sources, you should be able to avoid these threats.

An up-to-date operating system and an always-on virus scanner will protect you even better from Trojans.

These security solutions protect against Trojans and other online threats:
Kaspersky Premium

Trojan Virus Removal

Related Articles:

Detecting ransomware – how encryption Trojans differ

Tips on avoiding phishing

Ransomware protection – how to keep your data safe


Share with your friends




Related articles

HTML Attachments: A Gateway for Malware?
Malicious HTML attachments have become a popular...
Understanding BlackCat ransomware: Threat overview and protective measures
Learn more about BlackCat ransomware with its...
Black Friday Scams: How to Shop Safely Online
Worried about Black Friday Scams whilst shopping...
What is a dark web scan?
Dark web scanning can be useful for protecting...
The Biggest Crypto Exchange Hacks: How to Make Sure You Protect Your Crypto Against Hacks
Learn how the biggest cryptocurrency hacks were...
What Can Hackers Do With Your Email Address?
Today, email addresses are a part of our digital...
What is SIM Swapping?
With SIM swapping on the rise, phone owners...
How to get rid of a calendar virus on different devices
Receiving strange notifications in your iPhone...
What Are eWallets and How Safe Are They?
Wondering about using eWallet apps and if phone...
I’m a phishing victim! What do I do now?
Phishing has become more prevalent over the past...
")
language="en"
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("welcome.mp3")
os.system=("start welcome.mp3")


