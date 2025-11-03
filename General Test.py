import time, sys, random, os


#NATIVE FUNCTIONS
def questionPick(qpool, apool):
    question = random.randrange(0, (len(qpool) - 1))
    print(qpool[question])
    correct = apool[question]
    guess = input()
    if correct == guess:
        return True
    else:
        return False

def clearScreen():
    os.system("clear")

def goodAnswer(correct, given):
    if correct == 0:
        decimal = 0
    else:
        decimal = (correct / given)
        if decimal >= 0.75:
            testPass = True
        else:
            testPass = False
    print( str(correct) + " out of " + str(given) + " - " + str((decimal * 100)) )
    time.sleep(1.50)
    if testPass == True:
        print( "Congratulations! You passed this section!" )
    else:
        print( "You did not pass this section. Better luck next time!" )
    time.sleep(1.50)



correct = 0

#QUESTIONS
G1A01 = """
G1A01. On which HF and/or MF amateur bands are there portions where General class licensees cannot transmit?
a. 60 meters, 30 meters, 17 meters, and 12 meters
b. 160 meters, 60 meters, 15 meters, and 12 meters
c. 80 meters, 40 meters, 20 meters, and 15 meters
d. 80 meters, 20 meters, 15 meters, and 10 meters
        """
G1A02 = """
G1A02. On which of the following bands is phone operation prohibited?
a. 160 meters
b. 30 meters
c. 17 meters
d. 12 meters
        """
G1A03 = """
G1A03. On which of the following bands is image transmission prohibited?
a. 160 meters
b. 30 meters
c. 20 meters
d. 12 meters
        """
G1A04 = """
G1A04. Which of the following amateur bands is restricted to communication only on specific channels, rather than frequency ranges?
a. 11 meters
b. 12 meters
c. 30 meters
d. 60 meters
        """
G1A05 = """
G1A05. On which of the following frequencies are General class licensees prohibited from operating as control operator?
a. 7.125 MHz to 7.175 MHz
b. 20.000 MHz to 28.025 MHz
c. 21.275 MHz to 21.300 MHz
d. All of the above
        """
G1A06 = """
G1A06. Which of the following applies when the FCC rules designate the amateur service as a secondary user on a band?
a. Amateur stations must record the call sign of the primary service station before operating on a frequency assigned to that station
b. Amateur stations may use the band only during emergencies
c. Amateur stations must not cause harmful interference to primary users and must accept interference from primary users
d. Amateur stations may only operate during specific hours of the day, while primary users are permitted 24-hour use of the band
        """
G1A07 = """
G1A07. On which amateur frequencies in the 10-meter band may stations with a General class control operator transmit CW emissions?
a. 28.000 MHz to 28.025 MHz only
b. 28.000 MHz to 28.300 MHz only
c. 28,025 MHz to 28.300 MHz only
d. The entire band
        """
G1A08 = """
G1A08. Which HF bands have segemnts exclusively allocated to Aateur Extra licensees?
a. All HF bands
b. 80 meters, 40 meters, 20 meters, and 15 meters
c. All HF bands exept 160 meters and 10 meters
d. 60 meters, 30 meters, 17 meters, and 12 meters
        """
G1A09 = """
G1A09. Which of the following frequencies is within the General calss portion of the 15-meter band?
a. 14250 kHz
b. 18155 kHz
c. 21300 kHz
d. 24900 kHz
        """
G1A10 = """
G1A10. What portion of the 10-meter band is available for repeater use?
a. The entire band
b. The portion between 28.1 MHz and 28.2 MHz
c. The portion between 28.3 MHz and 28.5 MHz
d. The portion above 29.5 MHz
        """
G1A11 = """
G1A11. When General class licensees are not permitted to use the entire voice portion of a band, which portion of the voice segment is available to them?
a. The lower frequency portion
b. The upper frequency portion
c. The lower frequency portion on frequencies below 7.3 MHz, and the upper portion on frequencies above 14.150 MHz
d. The upper frequency portion on frequencies below 7.3 MHz, and the lower portion on frequencies above 14.150 MHz
        """
G1B01 = """
G1B01. What is the maximum height above ground for an antenna structure not near a public use airport without requiring notification to the FAA and registration with the FCC?
a. 50 feet
b. 100 feet
c. 200 feet
d. 250 feet
        """
G1B02 = """
G1B02. With which of the following conditions must beacon stations comply?
a. No more than one beacon station may transmit in the same band from the same station location
b. The frequency must be coordinated with the National Beacon Organization
c. The frequency must be posted on the internet or published in a natrional periodical
d. All these choices are correct
        """
G1B03 = """
G1B03. Which of the following conditions must beacon stations comply?
a. No more than one beacon station may transmit in the same band from the same station location
b. The frequency must be coordinated with the National Beacon Organization
c. The frequency must be posted on the internet or published in a national periodical
d. All these choices are correct
        """
G1B04 = """
G1B04. Which of the following transmissions is permitted for all amateur stations?
a. Unidentified transimssions of less than 10 seconds duration for test purposes only 
b. Automatic retransmission of other amateur signals by any amateur station
c. Occasional retransmission of weather and propagation forecast information from US government stations
d. encrypted messages, if not intended to facilitate a criminal act
        """
G1B05 = """
G1B05. Which of the following one-way transmissions are permitted?
a. Unidentified test transmissions of less than 10 seconds in duration
b. Transmissions to assist with learning the International Morse code
c. Regular transmissions offering equipment for sale, if intended for amateur radio use
d. All of these are correct
        """
G1B06 = """
G1B06. Under what conditions are state and local governments permitted to regulate amateur radio antenna structures?
a. Under no circumstances, FCC rules take priority
b. At any time and to any extent necessary to accomplish a legitimate purpose of the state or local entity, provided that proper filings are made with the FCC
c. Only when such structures exceed 50 feet in height and are clearly visible 1,000 feet from the structure
d. Amateur Service communications must be reasonably accommodated, and regulations must constitute the minimum practical to accommodate a legitimate purpose of the state or local entity
        """
G1B07 = """
G1B07. What are the restrictions on the use of abbreviations or procedural signals in the amateur service?
a. Only "Q" signals are permitted
b. They may be used if they do not obscure the meaning of a message
c. They are not permitted
d. They are limited to those expressly listed in Part 97 of the FCC rules
        """
G1B08 = """
G1B08. When is it permissible to communicate with amateur stations in countries outside the areas administered by the Federal Communications Commission?
a. Only when the foreign country has a formal third-party agreement filed with the FCC
b. When the contact is with amateurs in any country except those whose administrations have notified the ITU that they object to such communications
c. Only when the contact is with amateurs licensed by a country which is a member of the United Nations, or by a territory possessed by such a country
d. Only when the contact is with amateurs licensed by a country which is a member of the International Amateur Radio Union, or by a territory possessed by such a country
        """
G1B09 = """
G1B09. On what HF frequencies are automatically controlled beacons permitted?
a. On any frequency if power is less than 1 watt
b. On any frequency if transmissions are in Morse code
c. 21.08 MHz to 21.09 MHz
d. 28.20 MHz to 28.30 MHz
        """
G1B10 = """
G1B10. What is the power limit for beacon stations?
a. 10 watts PEP output
b. 20 watts PEP output
c. 100 watts PEP output
d. 200 watts PEP output
        """
G1B11 = """
G1B11. Who or what determines "good engineering and good amateur practice," as applied to the operation of an amateur station in all respects not covered by the Part 97 rules?
a. The FCC
b. The control operator
c. The IEEE
d. The ITU
        """

G1C01 = """
G1C01. What is the maximum transmitter power an amateur station may use on 10.140 MHz?
a. 200 watts PEP output
b. 1000 watts PEP output
c. 1500 watts PEP output
d. 2000 watts PEP output
        """
G1C02 = """
G1C02. What is the maximum transmitter power an amateur station may use on the 12-meter band?
a. 50 watts PEP output
b. 200 watts PEP output
c. 15000 watts PEP output
d. An effective radiated power equivalent to 100 watts from a half-wave dipole
        """
G1C03 = """
G1C03. What is the maximum bandwidth permitted by FCC rules for amateur radio stations transmitting on USB frequencies in the 60-meter band?
a. 2.8 kHz
b. 5.6 kHz
c. 1.8 kHz
d. 3 kHz
        """
G1C04 = """
G1C04. Which of the following is required by the FCC rules when operating in the 60-meter band?
a. If you are using an antenna other than a dipole, you must keep a record of the gain in your antenna
b. You must keep a record of the date, time, frequency, power level, and stations worked
c. You must keep a record of all third-party traffic
d. You must keep a record of the manufacturer of your equipment and the antenna used
        """
G1C05 = """
G1C05. What is the limit for transmitter power on the 28 MHz band for a General Class control operator?
a. 100 watts PEP output
b. 1000 watts PEP output
c. 1500 watts PEP output
d. 2000 watts PEP output
    """
G1C06 = """
G1C06. What is the limit for transmitter power on the 1.8 MHz band?
a. 200 watts PEP output
b. 1000 watts PEP output
c. 1200 watts PEP output
d. 1500 watts PEP output
    """
G1C07 = """
G1C07. What must be done before using a new digital protocol on the air?
a. Type-certify equipment to FCC standards
b. Obtain an experimental license from the FCC
c. Publicly document the technical characteristics of the protogol
d. Submit a rule-making proposal to the FCC describing the codes and methods of the technique
        """
G1C08 = """
G1C08. What is the maximum symbol rate permitted for RTTY or data emission transmitted at frequencies below 28 MHz?
a. 56 kilobaud
b. 19.6 kilobaud
c. 1200 baud
d. 300 baud
        """
G1C09 = """
G1C09. What is the maximum power limit on the 60-meter band?
a. 1500 watts PEP
b. 10 watts RMS
c. ERP of 100 watts PEP with respect to a dipole
d. ERP of 100 watts PEP with respect to an isotropic antenna
        """
G1C10 = """
G1C10. What is the maximum symbol rate permitted for RTTY or data emission transmissions on the 10-meter band?
a. 56 kilobaud
b. 19.6 kilobaud
c. 1200 baud
d. 300 baud
        """
G1C11 = """
G1C11. What measurement is specified by FCC rules that regulate maximum power?
a. RMS output from the transmitter
b. RMS input to the antenna
c. PEP input to the antenna
d. PEP output from the transmitter
        """

G1D01 = """
G1D01. Who may receive partial credit for the elements represented by an expired amateur radio license?
a. Any person who can demonstrate that they once held an FCC-issued General, Advanced, or Amateur Extra class license that was not revoked by the FCC
b. Anyone who held an FCC-issued amateur radio license that expired not less than 5 and not more than 15 years ago
c. Any person who previously held an amateur license issued by another country, but only if that country has a current reciprocal licensing agreement with the FCC
d. Only persons who once helled an FCC issued Novice, Technician, or Technician Plus license
        """
G1D02 = """
G1D02. What license examinations may you administer as an accredited Volunteer Examiner holding a General class operator license?
a. General and Technician
b. None, only Amateur Extra class licensees may be accredited
c. Technician only
d. Amateur Extra, General, and Technician
        """
G1D03 = """
G1D03. On which of the following band segments may you operate if you are a Technician class operator and have an unexpired Certificate of Successful Completion of Examination (CSCE) for General class privileges?
a. Only the Technician band segments until your upgrade is posted in the FCC database
b. Only on the Technician band segments until your upgrade is posted in the FCC database
c. On any General or Technician class band segment
d. Amateur Extra, General, and Technician
        """
G1D04 = """
G1D04. Who must observe the administration of a Technician class license examination?
a. At least three Volunteer Examiners of General class or higher
b. At least two Volunteer Examiners of General class or higher
c. At least two Volunteer Examiners of Technician class or higher
d. At least htree Volunteer examiners of Technician class
        """
G1D05 = """
G1D05. When operating a US station by remote control from outside the country, what license is required of the control operator?
a. A US operator/primary station license
b. Only an appropriate US operator/primary license and a special remote station permit from the FCC
c. Only a license from the foreign country, as long as the call sign includes identification of portable operation in the US
d. A license from the foreign country and a special remote station permit from the FCC        
    """
G1D06 = """
G1D06. Until an upgrade to General class is shown in the FCC database, when must a Technician licensee identify with "AG" after their call sign?
a. Whenever they operate using General class frequency privileges
b. whenever they operate on any amateur frequency
c. Whenever they operate using Technician frequency privileges
d. A special identifier is not required if their General class license application has been filed with the FCC
        """
G1D07 = """
G1D07. Volunteer Examiners are accredited by what organization?
a. The Federal Communications Commissoin
b. The Universal Licensing System
c. A Volunteer Examiner Coordinator
d. The Wireless Telecommunications Bureau
        """
G1D08 = """
G1D08. Which of the following criteria must be met for a non-US citizen to be an accredited Volunteer Examiner?
a. The person must be a resident of the US for a minimum of 5 years
b. The person must hold an FCC granted amateur radio license of General class or above
c. The person's home citizenship must be in ITU region 2
d. None of these choices is correct; a nonpUS citizen cannot be a Volunteer Examiner
        """
G1D09 = """
G1D09. How long is a Certificate of Successful Completion of Examination (CSCE) valid for exam element credit?
a. 30 days
b. 180 days
c. 365 days
d. For as long as your current license is valid
        """
G1D10 = """
G1D10. What is the minimum age that one must be to qualify as an accredited Volunteer Examiner?
a. 16 years
b. 18 years
c. 21 years
d. There is no age limit
        """
G1D11 = """
G1D11. What action is required to obtain a new General class license after a previously held license has expired and the two-year grace period has passed?
a. They must have a letter from the FCC showing they once held an amateur or commercial license
b. There are no requirements other than being able to show a copy of the expired license
c. Contact the FCC to have the license reinstated
d. The applicant must show proof of the appropriate expired license grand and pass the current Element 2 exam
        """
G1D12 = """
G1D12. When operating a station in South America by remote control over the internet from the US, what regulations apply?
a. Those of both the remote station's country and the FCC
b. Those of the remote station's country and the FCC's third-party regulations
c. Only those of the remote station's country
d. Only those of the FCC
        """

G1E01 = """
G1E01. Which of the following would disqualify a third party from participating in sending a message via an amateur station?
a. The third party's amateur license has been revoked and not reinstated
b. The third party is not a US citizen
c. The third party is speaking in a language other than English
d. All these choices are correct
        """
G1E02 = """
G1E02. When may a 10-meter repeater retransmit the 2-meter signal from a station that has a Technician class control operator?
a. Under no circumstances
b. Only if the station on 10-meters is operating under a Special Temporary Authorization allowing such retransmission
c. Only during an FCC-declared general state of communications emergency
d. Only if the 10-meter repeater control operator holds at least a General class license
        """
G1E03 = """
G1E03. What is required to conduct communications with a digital station operating under automatic control outside the automatic control band segments?
A. The station initiating the contact must be under local or remote control
B. The interrogating transmission must be made by another automatically controlled station
C. No third-party traffic may be transmitted
D. The control operator of the interrogating station must hold an Amateur Extra class license 
        """
G1E04 = """
G1E04. Which of the following conditions require a licensed amateur radio operator to take specific steps to avoid harmful interference to other users or facilities?
A. When operating within one mile of an FCC Monitoring Station
B. When using a band where the Amateur Service is secondary
C. When a station is transmitting spread spectrum emissions
D. All these choices are correct
        """
G1E05 = """G1E05. What are the restrictions on messages sent to a third party in a country with which there is a Third-Party Agreement?
A. They must relate to emergencies or disaster relief
B. They must be for other licensed amateurs
C. They must relate to amateur radio, or remarks of a personal character, or messages relating to emergencies or disaster relief
D. The message must be limited to no longer than 1 minute in duration and the name of the third party must be recorded in the station log
        """
G1E06 = """
G1E06. The frequency allocations of which ITU region apply to radio amateurs operating in North and South America?
A. Region 4
B. Region 3
C. Region 2
D. Region 1
        """
G1E07 = """
G1E07. In what part of the 2.4 GHz band may an amateur station communicate with non-licensed Wi-Fi stations?
A. Anywhere in the band
B. Channels 1 through 4
C. Channels 42 through 45
D. No part
        """
G1E08 = """
G1E08. What is the maximum PEP output allowed for spread spectrum transmissions?
A. 100 milliwatts
B. 10 watts
C. 100 watts
D. 1500 watts
        """
G1E09 = """
G1E09. Under what circumstances are messages that are sent via digital modes exempt from Part 97 third-party rules that apply to other modes of communication?
A. Under no circumstances
B. When messages are encrypted
C. When messages are not encrypted
D. When under automatic control
        """
G1E10 = """
G1E10. Why should an amateur operator normally avoid transmitting on 14.100, 18.110, 21.150, 24.930 and 28.200 MHz?
A. A system of propagation beacon stations operates on those frequencies
B. A system of automatic digital stations operates on those frequencies 
C. These frequencies are set aside for emergency operations
D. These frequencies are set aside for bulletins from the FCC
        """
G1E11 = """
G1E11. On what bands may automatically controlled stations transmitting RTTY or data emissions communicate with other automatically controlled digital stations?
A. On any band segment where digital operation is permitted
B. Anywhere in the non-phone segments of the 10-meter or shorter wavelength bands
C. Only in the non-phone Extra Class segments of the bands
D. Anywhere in the 6-meter or shorter wavelength bands, and in limited segments of some of the HF bands
        """
G1E12 = """
G1E12. When may third-party messages be transmitted via remote control?
A. Under any circumstances in which third party messages are permitted by FCC rules
B. Under no circumstances except for emergencies
C. Only when the message is intended for licensed radio amateurs
D. Only when the message is intended for third parties in areas where licensing is controlled by the FCC
        """






G2A01 = """
G2A0. Which mode is most commonly used for voice communications on frequencies of 14 MHz or higher?
A. Upper sideband
B. Lower sideband
C. Suppressed sideband
D. Double sideband
        """
G2A02 = """
G2A02. Which mode is most commonly used for voice communications on the 160-, 75-, and 40-meter bands?
A. Upper sideband
B. Lower sideband
C. Suppressed sideband
D. Double sideband
        """
G2A03 = """
G2A03. Which mode is most commonly used for SSB voice communications in the VHF and UHF bands?
A. Upper sideband
B. Lower sideband
C. Suppressed sideband
D. Double sideband
        """
G2A04 = """
G2A04. Which mode is most commonly used for voice communications on the 17- and 12-meter bands?
A. Upper sideband
B. Lower sideband
C. Suppressed sideband
D. Double sideband
        """
G2A05 = """
G2A05. Which mode of voice communication is most commonly used on the HF amateur bands?
A. Frequency modulation
B. Double sideband
C. Single sideband
D. Single phase modulation
        """
G2A06 = """
G2A06. Which of the following is an advantage of using single sideband, as compared to other analog voice modes on the HF amateur bands?
A. Very high-fidelity voice modulation
B. Less subject to interference from atmospheric static crashes
C. Ease of tuning on receive and immunity to impulse noise
D. Less bandwidth used and greater power efficiency
        """
G2A07 = """
G2A07. Which of the following statements is true of single sideband (SSB)?
A. Only one sideband and the carrier are transmitted; the other sideband is suppressed
B. Only one sideband is transmitted; the other sideband and carrier are suppressed
C. SSB is the only voice mode authorized on the 20-, 15-, and 10-meter amateur bands
D. SSB is the only voice mode authorized on the 160-, 75-, and 40-meter amateur bands
        """
G2A08 = """
G2A08. What is the recommended way to break into a phone contact?
A. Say “QRZ” several times, followed by your call sign
B. Say your call sign once
C. Say “Breaker Breaker”
D. Say “CQ” followed by the call sign of either station
        """
G2A09 = """
G2A09. Why do most amateur stations use lower sideband on the 160-, 75-, and 40-meter bands?
A. Lower sideband is more efficient than upper sideband at these frequencies
B. Lower sideband is the only sideband legal on these frequency bands
C. Because it is fully compatible with an AM detector
D. It is commonly accepted amateur practice
        """
G2A10 = """
G2A10. Which of the following statements is true of VOX operation versus PTT operation?
A. The received signal is more natural sounding
B. It allows “hands free” operation
C. It occupies less bandwidth
D. It provides more power output
        """
G2A11 = """
G2A11. Generally, who should respond to a station in the contiguous 48 states calling “CQ DX”?
A. Any caller is welcome to respond
B. Only stations in Germany
C. Any stations outside the lower 48 states
D. Only contest stations
        """
G2A12 = """
G2A12. What control is typically adjusted for proper ALC setting on a single sideband transceiver?
A. RF clipping level
B. Transmit audio or microphone gain
C. Antenna inductance or capacitance
D. Attenuator level
        """

G2B01 = """
G2B01. Which of the following is true concerning access to frequencies?
A. Nets have priority
B. QSOs in progress have priority
C. Except during emergencies, no amateur station has priority access to any frequency
D. Contest operations should yield to non-contest use of frequencies
        """
G2B02 = """
G2B02. What is the first thing you should do if you are communicating with another amateur station and hear a station in distress break in?
A. Inform your local emergency coordinator
B. Acknowledge the station in distress and determine what assistance may be needed
C. Immediately decrease power to avoid interfering with the station in distress
D. Immediately cease all transmissions
        """
G2B03 = """
G2B03. What is good amateur practice if propagation changes during a contact creating interference from other stations using the frequency?
A. Advise the interfering stations that you are on the frequency and that you have priority
B. Decrease power and continue to transmit
C. Attempt to resolve the interference problem with the other stations in a mutually acceptable manner
D. Switch to the opposite sideband
        """
G2B04 = """
G2B04. When selecting a CW transmitting frequency, what minimum separation from other stations should be used to minimize interference to stations on adjacent frequencies?
A. 5 Hz to 50 Hz
B. 150 Hz to 500 Hz
C. 1 kHz to 3 kHz
D. 3 kHz to 6 kHz
        """
G2B05 = """
G2B05. When selecting an SSB transmitting frequency, what minimum separation should be used to minimize interference to stations on adjacent frequencies?
A. 5 Hz to 50 Hz
B. 150 Hz to 500 Hz
C. 2 kHz to 3 kHz
D. Approximately 6 kHz
    """
G2B06 = """
G2B06. How can you avoid harmful interference on an apparently clear frequency before calling CQ on CW or phone?
A. Send “QRL?” on CW, followed by your call sign; or, if using phone, ask if the frequency is in use, followed by your call sign
B. Listen for 2 minutes before calling CQ
C. Send the letter “V” in Morse code several times and listen for a response, or say “test” several times and listen for a response
D. Send “QSY” on CW or if using phone, announce “the frequency is in use,” then give your call sign and listen for a response
        """
G2B07 = """
G2B07. Which of the following complies with commonly accepted amateur practice when choosing a frequency on which to initiate a call?
A. Listen on the frequency for at least two minutes to be sure it is clear
B. Identify your station by transmitting your call sign at least 3 times
C. Follow the voluntary band plan
D. All these choices are correct
        """
G2B08 = """
G2B08. What is the voluntary band plan restriction for US stations transmitting within the 48 contiguous states in the 50.1 MHz to 50.125 MHz band segment?
A. Only contacts with stations not within the 48 contiguous states
B. Only contacts with other stations within the 48 contiguous states
C. Only digital contacts
D. Only SSTV contacts
        """
G2B09 = """
G2B09. Who may be the control operator of an amateur station transmitting in RACES to assist relief operations during a disaster?
A. Only a person holding an FCC-issued amateur operator license
B. Only a RACES net control operator
C. A person holding an FCC-issued amateur operator license or an appropriate government official
D. Any control operator when normal communication systems are operational
        """
G2B10 = """
G2B10. Which of the following is good amateur practice for net management?
A. Always use multiple sets of phonetics during check-in
B. Have a backup frequency in case of interference or poor conditions
C. Transmit the full net roster at the beginning of every session
D. All these choices are correct
        """
G2B11 = """
G2B11. How often may RACES training drills and tests be routinely conducted without special authorization?
A. No more than 1 hour per month
B. No more than 2 hours per month
C. No more than 1 hour per week
D. No more than 2 hours per week
        """

G2C01 = """
G2C01. Which of the following describes full break-in CW operation (QSK)?
A. Breaking stations send the Morse code prosign “BK”
B. Automatic keyers, instead of hand keys, are used to send Morse code
C. An operator must activate a manual send/receive switch before and after every transmission
D. Transmitting stations can receive between code characters and elements
        """
G2C02 = """
G2C02. What should you do if a CW station sends “QRS?”
A. Send slower
B. Change frequency
C. Increase your power
D. Repeat everything twice
        """
G2C03 = """
G2C03. What does it mean when a CW operator sends “KN” at the end of a transmission?
A. No US stations should call
B. Operating full break-in
C. Listening only for a specific station or stations
D. Closing station now
        """
G2C04 = """
G2C04. What does the Q signal “QRL?” mean?
A. “Will you keep the frequency clear?”
B. “Are you operating full break-in?” or “Can you operate full break-in?”
C. “Are you listening only for a specific station?”
D. “Are you busy?” or “Is this frequency in use?”
        """
G2C05 = """
G2C05. What is the best speed to use when answering a CQ in Morse code?
A. The fastest speed at which you are comfortable copying, but no slower than the CQ
B. The fastest speed at which you are comfortable copying, but no faster than the CQ
C. At the standard calling speed of 10 wpm
D. At the standard calling speed of 5 wpm
        """
G2C06 = """
G2C06. What does the term “zero beat” mean in CW operation?
A. Matching the speed of the transmitting station
B. Operating split to avoid interference on frequency
C. Sending without error
D. Matching the transmit frequency to the frequency of a received signal
        """
G2C07 = """
G2C07. When sending CW, what does a “C” mean when added to the RST report?
A. Chirpy or unstable signal
B. Report was read from an S meter rather than estimated
C. 100 percent copy
D. Key clicks
        """
G2C08 = """
G2C08. What prosign is sent to indicate the end of a formal message when using CW?
A. SK
B. BK
C. AR
D. KN
        """
G2C09 = """
G2C09. What does the Q signal “QSL” mean?
A. Send slower
B. We have already confirmed the contact
C. I have received and understood
D. We have worked before
        """
G2C10 = """
G2C10. What does the Q signal “QRN” mean?
A. Send more slowly
B. Stop sending
C. Zero beat my signal
D. I am troubled by static
        """
G2C11 = """
G2C11. What does the Q signal “QRV” mean?
A. You are sending too fast
B. There is interference on the frequency
C. I am quitting for the day
D. I am ready to receive
        """

G2D01 = """
G2D01. What is the Volunteer Monitor Program?
A. Amateur volunteers who are formally enlisted to monitor the airwaves for rules violations
B. Amateur volunteers who conduct amateur licensing examinations
C. Amateur volunteers who conduct frequency coordination for amateur VHF repeaters
D. Amateur volunteers who use their station equipment to help civil defense organizations in times of emergency
        """
G2D02 = """
G2D02. Which of the following are objectives of the Volunteer Monitor Program?
A. To conduct efficient and orderly amateur licensing examinations
B. To provide emergency and public safety communications
C. To coordinate repeaters for efficient and orderly spectrum usage
D. To encourage amateur radio operators to self-regulate and comply with the rules
        """
G2D03 = """
G2D03. What procedure may be used by Volunteer Monitors to localize a station whose continuous carrier is holding a repeater on in their area?
A. Compare vertical and horizontal signal strengths on the input frequency
B. Compare beam headings on the repeater input from their home locations with that of other Volunteer Monitors
C. Compare signal strengths between the input and output of the repeater
D. All these choices are correct
        """
G2D04 = """
G2D04. Which of the following describes an azimuthal projection map?
A. A map that shows accurate land masses
B. A map that shows true bearings and distances from a specific location
C. A map that shows the angle at which an amateur satellite crosses the equator
D. A map that shows the number of degrees longitude that an amateur satellite appears to move westward at the equator with each orbit
        """
G2D05 = """
G2D05. Which of the following indicates that you are looking for an HF contact with any station?
A. Sign your call sign once, followed by the words “listening for a call” -- if no answer, change frequency and repeat
B. Say “QTC” followed by “this is” and your call sign -- if no answer, change frequency and repeat
C. Repeat “CQ” a few times, followed by “this is,” then your call sign a few times, then pause to listen, repeat as necessary
D. Transmit an unmodulated carried for approximately 10 seconds, followed by “this is” and your call sign, and pause to listen -- repeat as necessary
        """
G2D06 = """
G2D06. How is a directional antenna pointed when making a “long-path” contact with another station?
A. Toward the rising sun
B. Along the gray line
C. 180 degrees from the station’s short-path heading
D. Toward the north
        """
G2D07 = """
G2D07. Which of the following are examples of the NATO Phonetic Alphabet?
A. Able, Baker, Charlie, Dog
B. Adam, Boy, Charles, David
C. America, Boston, Canada, Denmark
D. Alpha, Bravo, Charlie, Delta
        """
G2D08 = """
G2D08. Why do many amateurs keep a station log?
A. The FCC requires a log of all international contacts
B. The FCC requires a log of all international third-party traffic
C. The log provides evidence of operation needed to renew a license without retest
D. To help with a reply if the FCC requests information about your station
        """
G2D09 = """
G2D09. Which of the following is required when participating in a contest on HF frequencies?
A. Submit a log to the contest sponsor
B. Send a QSL card to the stations worked, or QSL via Logbook of The World
C. Identify your station according to normal FCC regulations
D. All these choices are correct
        """
G2D10 = """
G2D10. What is QRP operation?
A. Remote piloted model control
B. Low-power transmit operation
C. Transmission using Quick Response Protocol
D. Traffic relay procedure net operation
        """
G2D11 = """
G2D11. Why are signal reports typically exchanged at the beginning of an HF contact?
A. To allow each station to operate according to conditions
B. To be sure the contact will count for award programs
C. To follow standard radiogram structure
D. To allow each station to calibrate their frequency display
        """

G2E01 = """
G2E01. Which mode is normally used when sending RTTY signals via AFSK with an SSB transmitter?
A. USB
B. DSB
C. CW
D. LSB
        """
G2E02 = """
G2E02. What is VARA?
A. A low signal-to-noise digital mode used for EME (moonbounce)
B. A digital protocol used with Winlink
C. A radio direction finding system used on VHF and UHF
D.A DX spotting system using a network of software defined radios
        """
G2E03 = """
G2E03. What symptoms may result from other signals interfering with a PACTOR or VARA transmission?
A. Frequent retries or timeouts
B. Long pauses in message transmission
C. Failure to establish a connection between stations
D. All these choices are correct
        """
G2E04 = """
G2E04. Which of the following is good practice when choosing a transmitting frequency to answer a station calling CQ using FT8?
A. Always call on the station’s frequency
B. Call on any frequency in the waterfall except the station’s frequency
C. Find a clear frequency during the same time slot as the calling station
D. Find a clear frequency during the alternate time slot to the calling station
        """
G2E05 = """
G2E05. What is the standard sideband for JT65, JT9, FT4, or FT8 digital signal when using AFSK?
A. LSB
B. USB
C. DSB
D. SSB
        """
G2E06 = """
G2E06. What is the most common frequency shift for RTTY emissions in the amateur HF bands?
A. 85 Hz
B. 170 Hz
C. 425 Hz
D. 850 Hz
        """
G2E07 = """
G2E07. Which of the following is required when using FT8?
A. A special hardware modem
B. Computer time accurate to within approximately 1 second
C. Receiver attenuator set to -12 dB
D. A vertically polarized antenna
        """
G2E08 = """
G2E08. In what segment of the 20-meter band are most digital mode operations commonly found?
A. At the bottom of the slow-scan TV segment, near 14.230 MHz
B. At the top of the SSB phone segment, near 14.325 MHz
C. In the middle of the CW segment, near 14.100 MHz
D. Between 14.070 MHz and 14.100 MHz
        """
G2E09 = """
G2E09. How do you join a contact between two stations using the PACTOR protocol?
A. Send broadcast packets containing your call sign while in MONITOR mode
B. Transmit a steady carrier until the PACTOR protocol times out and disconnects
C. Joining an existing contact is not possible, PACTOR connections are limited to two stations
D. Send a NAK code
        """
G2E10 = """
G2E10. Which of the following is a way to establish contact with a digital messaging system gateway station?
A. Send an email to the system control operator
B. Send QRL in Morse code
C. Respond when the station broadcasts its SSID
D. Transmit a connect message on the station’s published frequency
        """
G2E11 = """
G2E11. What is the primary purpose of an Amateur Radio Emergency Data Network (AREDN) mesh network?
A. To provide FM repeater coverage in remote areas
B. To provide real time propagation data by monitoring amateur radio transmissions worldwide
C. To provide high-speed data services during an emergency or community event
D. To provide DX spotting reports to aid contesters and DXers
        """
G2E12 = """
G2E12. Which of the following describes Winlink?
A. An amateur radio wireless network to send and receive email on the internet
B. A form of Packet Radio
C. A wireless network capable of both VHF and HF band operation
D. All of the above
        """
G2E13 = """
G2E13. What is another name for a Winlink Remote Message Server?
A. Terminal Node Controller
B. Gateway
C. RJ-45
D. Printer/Server
        """
G2E14 = """
G2E14. What could be wrong if you cannot decode an RTTY or other FSK signal even though it is apparently tuned in properly?
A. The mark and space frequencies may be reversed
B. You may have selected the wrong baud rate
C. You may be listening on the wrong sideband
D. All these choices are correct
        """
G2E15 = """
G2E15. Which of the following is a common location for FT8?
A. Anywhere in the voice portion of the band
B. Anywhere in the CW portion of the band
C. Approximately 14.074 MHz to 14.077 MHz
D. Approximately 14.110 MHz to 14.113 MHz
        """



G3A01 = """
G3A01. How does a higher sunspot number affect HF propagation?
A. Higher sunspot numbers generally indicate a greater probability of good propagation at higher frequencies
B. Lower sunspot numbers generally indicate greater probability of sporadic E propagation
C. A zero sunspot number indicates that radio propagation is not possible on any band
D. A zero sunspot number indicates undisturbed conditions
        """
G3A02 = """
G3A02. What effect does a sudden ionospheric disturbance have on the daytime ionospheric propagation?
A. It enhances propagation on all HF frequencies
B. It disrupts signals on lower frequencies more than those on higher frequencies
C. It disrupts communications via satellite more than direct communications
D. None, because only areas on the night side of the Earth are affected
        """
G3A03 = """
G3A03. Approximately how long does it take the increased ultraviolet and X-ray radiation from a solar flare to affect radio propagation on Earth?
A. 28 days
B. 1 to 2 hours
C. 8 minutes
D. 20 to 40 hours
        """
G3A04 = """
G3A04. Which of the following are the least reliable bands for long-distance communications during periods of low solar activity?
A. 80 meters and 160 meters
B. 60 meters and 40 meters
C. 30 meters and 20 meters
D. 15 meters, 12 meters, and 10 meters
        """
G3A05 = """
G3A05. What is the solar flux index?
A. A measure of the highest frequency that is useful for ionospheric propagation between two points on Earth
B. A count of sunspots that is adjusted for solar emissions
C. Another name for the American sunspot number
D. A measure of solar radiation with a wavelength of 10.7 centimeters
        """
G3A06 = """
G3A06. What is a geomagnetic storm?
A. A sudden drop in the solar flux index
B. A thunderstorm that affects radio propagation
C. Ripples in the geomagnetic force
D. A temporary disturbance in Earth’s geomagnetic field
        """
G3A07 = """
G3A07. At what point in the solar cycle does the 20-meter band usually support worldwide propagation during daylight hours?
A. At the summer solstice
B. Only at the maximum point
C. Only at the minimum point
D. At any point
        """
G3A08 = """
G3A08. How can a geomagnetic storm affect HF propagation?
A. Improve high-latitude HF propagation
B. Degrade ground wave propagation
C. Improve ground wave propagation
D. Degrade high-latitude HF propagation
        """
G3A09 = """
G3A09. How can high geomagnetic activity benefit radio communications?
A. Creates auroras that can reflect VHF signals
B. Increases signal strength for HF signals passing through the polar regions
C. Improve HF long path propagation
D. Reduce long delayed echoes
        """
G3A10 = """
G3A10. What causes HF propagation conditions to vary periodically in a 26- to 28-day cycle?
A. Long term oscillations in the upper atmosphere
B. Cyclic variation in Earth’s radiation belts
C. Rotation of the Sun’s surface layers around its axis
D. The position of the Moon in its orbit
        """
G3A11 = """
G3A11. How long does it take a coronal mass ejection to affect radio propagation on Earth?
A. 28 days
B. 14 days
C. 4 to 8 minutes
D. 15 hours to several days
        """
G3A12 = """
G3A12. What does the K-index measure?
A. The relative position of sunspots on the surface of the Sun
B. The short-term stability of Earth’s geomagnetic field
C. The short-term stability of the Sun’s magnetic field
D. The solar radio flux at Boulder, Colorado
        """
G3A13 = """
G3A13. What does the A-index measure?
A. The relative position of sunspots on the surface of the Sun
B. The amount of polarization of the Sun’s electric field
C. The long-term stability of Earth’s geomagnetic field
D. The solar radio flux at Boulder, Colorado
        """
G3A14 = """
G3A14. How is long distance radio communication usually affected by the charged particles that reach Earth from solar coronal holes?
A. HF communication is improved
B. HF communication is disturbed
C. VHF/UHF ducting is improved
D. VHF/UHF ducting is disturbed
        """

G3B01 = """
G3B01. What is a characteristic of skywave signals arriving at your location by both short-path and long-path propagation?
A. Periodic fading approximately every 10 seconds
B. Signal strength increased by 3 dB
C. The signal might be cancelled causing severe attenuation
D. A slightly delayed echo might be heard
        """
G3B02 = """
G3B02. What factors affect the MUF?
A. Path distance and location
B. Time of day and season
C. Solar radiation and ionospheric disturbances
D. All these choices are correct
        """
G3B03 = """
G3B03. Which frequency will have the least attenuation for long-distance skip propagation?
A. Just below the MUF
B. Just above the LUF
C. Just below the critical frequency
D. Just above the critical frequency
        """
G3B04 = """
G3B04. Which of the following is a way to determine current propagation on a desired band from your station?
A. Use a network of automated receiving stations on the internet to see where your transmissions are being received
B. Check the A-index
C. Send a series of dots and listen for echoes
D. All these choices are correct. 
        """
G3B05 = """
G3B05. How does the ionosphere affect radio waves with frequencies below the MUF and above the LUF?
A. They are refracted back to Earth
B. They pass through the ionosphere
C. They are amplified by interaction with the ionosphere
D. They are refracted and trapped in the ionosphere to circle Earth
        """
G3B06 = """
G3B06. What usually happens to radio waves with frequencies below the LUF?
A. They are refracted back to Earth
B. They pass through the ionosphere
C. They are attenuated before reaching the destination
D. They are refracted and trapped in the ionosphere to circle Earth
        """
G3B07 = """
G3B07. What does LUF stand for?
A. The Lowest Usable Frequency for communications between two specific points
B. Lowest Usable Frequency for communications to any point outside a 100-mile radius
C. The Lowest Usable Frequency during a 24-hour period
D. Lowest Usable Frequency during the past 60 minutes
        """
G3B08 = """
G3B08. What does MUF stand for?
A. The Minimum Usable Frequency for communications between two points
B. The Maximum Usable Frequency for communications between two points
C. The Minimum Usable Frequency during a 24-hour period
D. The Maximum Usable Frequency during a 24-hour period
        """
G3B09 = """
G3B09. What is the approximate maximum distance along the Earth’s surface normally covered in one hop using the F2 region?
A. 180 miles
B. 1,200 miles
C. 2,500 miles
D. 12,000 miles
        """
G3B10 = """
G3B10. What is the approximate maximum distance along the Earth’s surface normally covered in one hop using the E region?
A. 180 miles
B. 1,200 miles
C. 2,500 miles
D. 12,000 miles
        """
G3B11 = """
G3B11. What happens to HF propagation when the LUF exceeds the MUF?
A. Propagation via ordinary skywave communications is not possible over that path
B. HF communications over the path are enhanced
C. Double-hop propagation along the path is more common
D. Propagation over the path on all HF frequencies is enhanced
        """
G3B12 = """
G3B12. Which of the following is typical of the lower HF frequencies during the summer?
A. Poor propagation at any time of day
B. World-wide propagation during daylight hours
C. Heavy distortion on signals due to photon absorption
D. High levels of atmospheric noise or static
        """

G3C01 = """
G3C01. Which ionospheric region is closest to the surface of Earth?
A. The D region
B. The E region
C. The F1 region
D. The F2 region
        """
G3C02 = """
G3C02. What is meant by the term “critical frequency” at a given incidence angle?
A. The highest frequency which is refracted back to Earth
B. The lowest frequency which is refracted back to Earth
C. The frequency at which the signal-to-noise ratio approaches unity
D. The frequency at which the signal-to-noise ratio is 6 dB
        """
G3C03 = """
G3C03. Why is skip propagation via the F2 region longer than that via the other ionospheric regions?
A. Because it is the densest
B. Because of the Doppler effect
C. Because it is the highest
D. Because of temperature inversions
        """
G3C04 = """
G3C04. What does the term “critical angle” mean, as applied to radio wave propagation?
A. The long path azimuth of a distant station
B. The short path azimuth of a distant station
C. The lowest takeoff angle that will return a radio wave to Earth under specific ionospheric conditions
D. The highest takeoff angle that will return a radio wave to Earth under specific ionospheric conditions
        """
G3C05 = """
G3C05. Why is long-distance communication on the 40-, 60-, 80-, and 160-meter bands more difficult during the day?
A. The F region absorbs signals at these frequencies during daylight hours
B. The F region is unstable during daylight hours
C. The D region absorbs signals at these frequencies during daylight hours
D. The E region is unstable during daylight hours
        """
G3C06 = """
G3C06. What is a characteristic of HF scatter?
A. Phone signals have high intelligibility
B. Signals have a fluttering sound
C. There are very large, sudden swings in signal strength
D. Scatter propagation occurs only at night
        """
G3C07 = """
G3C07. What makes HF scatter signals often sound distorted?
A. The ionospheric region involved is unstable
B. Ground waves are absorbing much of the signal
C. The E region is not present
D. Energy is scattered into the skip zone through several different paths
        """
G3C08 = """
G3C08. Why are HF scatter signals in the skip zone usually weak?
A. Only a small part of the signal energy is scattered into the skip zone
B. Signals are scattered from the magnetosphere, which is not a good reflector
C. Propagation is via ground waves, which absorb most of the signal energy
D. Propagation is via ducts in the F region, which absorb most of the energy
        """
G3C09 = """
G3C09. What type of propagation allows signals to be heard in the transmitting station’s skip zone?
A. Faraday rotation
B. Scatter
C. Chordal hop
D. Short-path
        """
G3C10 = """
G3C10. What is near vertical incidence skywave (NVIS) propagation?
A. Propagation near the MUF
B. Short distance MF or HF propagation at high elevation angles
C. Long path HF propagation at sunrise and sunset
D. Double hop propagation near the LUF
        """
G3C11 = """
G3C11. Which ionospheric region is the most absorbent of signals below 10 MHz during daylight hours?
A. The F2 region
B. The F1 region
C. The E region
D. The D region
        """



G4A01 = """
G4A01. What is the purpose of the notch filter found on many HF transceivers?
A. To restrict the transmitter voice bandwidth
B. To reduce interference from carriers in the receiver passband
C. To eliminate receiver interference from impulse noise sources
D. To remove interfering splatter generated by signals on adjacent frequencies
        """
G4A02 = """
G4A02. What is the benefit of using the opposite or “reverse” sideband when receiving CW?
A. Interference from impulse noise will be eliminated
B. More stations can be accommodated within a given signal passband
C. It may be possible to reduce or eliminate interference from other signals
D. Accidental out-of-band operation can be prevented
        """
G4A03 = """
G4A03. How does a noise blanker work?
A. By temporarily increasing received bandwidth
B. By redirecting noise pulses into a filter capacitor
C. By reducing receiver gain during a noise pulse
D. By clipping noise peaks
        """
G4A04 = """
G4A04. What is the effect on plate current of the correct setting of a vacuum-tube RF power amplifier’s TUNE control?
A. A pronounced peak
B. A pronounced dip
C. No change will be observed
D. A slow, rhythmic oscillation
        """
G4A05 = """
G4A05. Why is automatic level control (ALC) used with an RF power amplifier?
A. To balance the transmitter audio frequency response
B. To reduce harmonic radiation
C. To prevent excessive drive
D. To increase overall efficiency
        """
G4A06 = """
G4A06. What is the purpose of an antenna tuner?
A. Reduce the SWR in the feed line to the antenna
B. Reduce the power dissipation in the feedline to the antenna
C. Increase power transfer from the transmitter to the feed line
D. All these choices are correct
        """
G4A07 = """
G4A07. What happens as a receiver’s noise reduction control level is increased?
A. Received signals may become distorted
B. Received frequency may become unstable
C. CW signals may become severely attenuated
D. Received frequency may shift several kHz
        """
G4A08 = """
G4A08. What is the correct adjustment for the LOAD or COUPLING control of a vacuum tube RF power amplifier?
A. Minimum SWR on the antenna
B. Minimum plate current without exceeding maximum allowable grid current
C. Highest plate voltage while minimizing grid current
D. Desired power output without exceeding maximum allowable plate current
        """
G4A09 = """
G4A09. What is the purpose of delaying RF output after activating a transmitter’s keying line to an external amplifier?
A. To prevent key clicks on CW
B. To prevent transient overmodulation
C. To allow time for the amplifier to switch the antenna between the transceiver and the amplifier output
D. To allow time for the amplifier power supply to reach operating level
        """
G4A10 = """
G4A10. What is the function of an electronic keyer?
A. Automatic transmit/receive switching
B. Automatic generation of dots and dashes for CW operation
C. To allow time for switching the antenna from the receiver to the transmitter
D. Computer interface for PSK and RTTY operation
        """
G4A11 = """
G4A11. Why should the ALC system be inactive when transmitting AFSK data signals?
A. ALC will invert the modulation of the AFSK mode
B. The ALC action distorts the signal
C. When using digital modes, too much ALC activity can cause the transmitter to overheat
D. All these choices are correct
        """
G4A12 = """
G4A12. Which of the following is a common use of the dual-VFO feature on a transceiver?
A. To allow transmitting on two frequencies at once
B. To permit full duplex operation -- that is, transmitting and receiving at the same time
C. To transmit on one frequency and listen on another
D. To improve frequency accuracy by allowing variable frequency output (VFO) operation
        """
G4A13 = """
G4A13. What is the purpose of using a receive attenuator?
A. To prevent receiver overload from strong incoming signals
B. To reduce the transmitter power when driving a linear amplifier
C. To reduce power consumption when operating from batteries
D. To reduce excessive audio level on strong signals
        """

G4B01 = """
G4B01. What item of test equipment contains horizontal and vertical channel amplifiers?
A. An ohmmeter
B. A signal generator
C. An ammeter
D. An oscilloscope
        """
G4B02 = """
G4B02. Which of the following is an advantage of an oscilloscope versus a digital voltmeter?
A. An oscilloscope uses less power
B. Complex impedances can be easily measured
C. Greater precision
D. Complex waveforms can be measured
        """
G4B03 = """
G4B03. Which of the following is the best instrument to use for checking the keying waveform of a CW transmitter?
A. An oscilloscope
B. A field strength meter
C. A sidetone monitor
D. A wavemeter
        """
G4B04 = """
G4B04. What signal source is connected to the vertical input of an oscilloscope when checking the RF envelope pattern of a transmitted signal?
A. The local oscillator of the transmitter
B. An external RF oscillator
C. The transmitter balanced mixer output
D. The attenuated RF output of the transmitter
        """
G4B05 = """
G4B05. Why do voltmeters have high input impedance?
A. It improves the frequency response
B. It allows for higher voltages to be safely measured
C. It improves the resolution of the readings
D. It decreases the loading on circuits being measured
        """
G4B06 = """
G4B06. What is an advantage of a digital multimeter as compared to an analog multimeter?
A. Better for measuring computer circuits
B. Less prone to overload
C. Higher precision
D. Faster response
        """
G4B07 = """
G4B07. What signals are used to conduct a two-tone test?
A. Two audio signals of the same frequency shifted 90 degrees
B. Two non-harmonically related audio signals
C. Two swept frequency tones
D. Two audio frequency range square wave signals of equal amplitude
        """
G4B08 = """
G4B08. What transmitter performance parameter does a two-tone test analyze?
A. Linearity
B. Percentage of suppression of the carrier and undesired sideband for SSB
C. Percentage of frequency modulation
D. Percentage of carrier phase shift
        """
G4B09 = """
G4B09. When is an analog multimeter preferred to a digital multimeter?
A. When testing logic circuits
B. When high precision is desired
C. When measuring the frequency of an oscillator
D. When adjusting circuits for maximum or minimum values
        """
G4B10 = """
G4B10. Which of the following can be determined with a directional wattmeter?
A. Standing wave ratio
B. Antenna front-to-back ratio
C. RF interference
D. Radio wave propagation
        """
G4B11 = """
G4B11. Which of the following must be connected to an antenna analyzer when it is being used for SWR measurements?
A. Receiver
B. Transmitter
C. Antenna and feed line
D. All these choices are correct
        """
G4B12 = """
G4B12. What effect can strong signals from nearby transmitters have on an antenna analyzer?
A. Desensitization which can cause intermodulation products which interfere with impedance readings
B. Received power that interferes with SWR readings
C. Generation of harmonics which interfere with frequency readings
D. All these choices are correct
        """
G4B13 = """
G4B13. Which of the following can be measured with an antenna analyzer?
A. Front-to-back ratio of an antenna
B. Power output from a transmitter
C. Impedance of coaxial cable
D. Gain of a directional antenna
        """
G4C01 = """
G4C01. Which of the following might be useful in reducing RF interference to audio frequency circuits?
A. Bypass inductor
B. Bypass capacitor
C. Forward-biased diode
D. Reverse-biased diode
        """
G4C02 = """
G4C02. Which of the following could be a cause of interference covering a wide range of frequencies?
A. Not using a balun or line isolator to feed balanced antennas
B. Lack of rectification of the transmitter's signal in power conductors
C. Arcing at a poor electrical connection
D. Using a balun to feed an unbalanced antenna
        """
G4C03 = """
G4C03. What sound is heard from an audio device experiencing RF interference from a single sideband phone transmitter?
A. A steady hum whenever the transmitter is on the air
B. On-and-off humming or clicking
C. Distorted speech
D. Clearly audible speech
        """
G4C04 = """
G4C04. What sound is heard from an audio device experiencing RF interference from a CW transmitter?
A. On-and-off humming or clicking
B. A CW signal at a nearly pure audio frequency
C. A chirpy CW signal
D. Severely distorted audio
        """
G4C05 = """
G4C05. What is a possible cause of high voltages that produce RF burns?
A. Flat braid rather than round wire has been used for the ground wire
B. Insulated wire has been used for the ground wire
C. The ground rod is resonant
D. The ground wire has high impedance on that frequency
        """
G4C06 = """
G4C06. What is a possible effect of a resonant ground connection?
A. Overheating of ground straps
B. Corrosion of the ground rod
C. High RF voltages on the enclosures of station equipment
D. A ground loop
        """
G4C07 = """
G4C07. Why should soldered joints not be used in lightning protection ground connections?
A. A soldered joint will likely be destroyed by the heat of a lightning strike
B. Solder flux will prevent a low conductivity connection
C. Solder has too high a dielectric constant to provide adequate lightning protection
D. All these choices are correct
        """
G4C08 = """
G4C08. Which of the following would reduce RF interference caused by common-mode current on an audio cable?
A. Place a ferrite choke on the cable
B. Connect the center conductor to the shield of all cables to short circuit the RFI signal
C. Ground the center conductor of the audio cable causing the interference
D. Add an additional insulating jacket to the cable
        """
G4C09 = """
G4C09. How can the effects of ground loops be minimized?
A. Connect all ground conductors in series
B. Connect the AC neutral conductor to the ground wire
C. Avoid using lock washers and star washers when making ground connections
D. Bond equipment enclosures together
        """
G4C10 = """
G4C10. What could be a symptom caused by a ground loop in your station’s audio connections?
A. You receive reports of “hum” on your station’s transmitted signal
B. The SWR reading for one or more antennas is suddenly very high
C. An item of station equipment starts to draw excessive amounts of current
D. You receive reports of harmonic interference from your station
        """
G4C11 = """
G4C11. What technique helps to minimize RF “hot spots” in an amateur station?
A. Building all equipment in a metal enclosure
B. Using surge suppressor power outlets
C. Bonding all equipment enclosures together
D. Placing low-pass filters on all feed lines
        """
G4C12 = """
G4C12. Why must all metal enclosures of station equipment be grounded?
A. It prevents a blown fuse in the event of an internal short circuit
B. It prevents signal overload
C. It ensures that the neutral wire is grounded
D. It ensures that hazardous voltages cannot appear on the chassis
        """
G4D01 = """
G4D01. What is the purpose of a speech processor in a transceiver?
A. Increase the apparent loudness of transmitted voice signals
B. Increase transmitter bass response for more natural-sounding SSB signals
C. Prevent distortion of voice signals
D. Decrease high-frequency voice output to prevent out-of-band operation
        """
G4D02 = """
G4D02. How does a speech processor affect a single sideband phone signal?
A. It increases peak power
B. It increases average power
C. It reduces harmonic distortion
D. It reduces intermodulation distortion
        """
G4D03 = """
G4D03. What is the effect of an incorrectly adjusted speech processor?
A. Distorted speech
B. Excess intermodulation products
C. Excessive background noise
D. All these choices are correct
        """
G4D04 = """
G4D04. What does an S meter measure?
A. Carrier suppression
B. Impedance
C. Received signal strength
D. Transmitter power output
        """
G4D05 = """
G4D05. How does a signal that reads 20 dB over S9 compare to one that reads S9 on a receiver, assuming a properly calibrated S meter?
A. It is 10 times less powerful
B. It is 20 times less powerful
C. It is 20 times more powerful
D. It is 100 times more powerful
        """
G4D06 = """
G4D06. How much change in signal strength is typically represented by one S unit?
A. 6 dB
B. 12 dB
C. 15 dB
D. 18 dB
        """
G4D07 = """
G4D07. How much must the power output of a transmitter be raised to change the S meter reading on a distant receiver from S8 to S9?
A. Approximately 1.5 times
B. Approximately 2 times
C. Approximately 4 times
D. Approximately 8 times
        """
G4D08 = """
G4D08. What frequency range is occupied by a 3 kHz LSB signal when the displayed carrier frequency is set to 7.178 MHz?
A. 7.178 MHz to 7.181 MHz
B. 7.178 MHz to 7.184 MHz
C. 7.175 MHz to 7.178 MHz
D. 7.1765 MHz to 7.1795 MHz
        """
G4D09 = """
G4D09. What frequency range is occupied by a 3 kHz USB signal with the displayed carrier frequency set to 14.347 MHz?
A. 14.347 MHz to 14.647 MHz
B. 14.347 MHz to 14.350 MHz
C. 14.344 MHz to 14.347 MHz
D. 14.3455 MHz to 14.3485 MHz
        """
G4D10 = """
G4D10. How close to the lower edge of a band’s phone segment should your displayed carrier frequency be when using 3 kHz wide LSB?
A. At least 3 kHz above the edge of the segment
B. At least 3 kHz below the edge of the segment
C. At least 1 kHz below the edge of the segment
D. At least 1 kHz above the edge of the segment
        """
G4D11 = """G4D11. How close to the upper edge of a band’s phone segment should your displayed carrier frequency be when using 3 kHz wide USB?
A. At least 3 kHz above the edge of the band
B. At least 3 kHz below the edge of the band
C. At least 1 kHz above the edge of the segment
D. At least 1 kHz below the edge of the segment
        """

G4E01 = """
G4E01. What is the purpose of a capacitance hat on a mobile antenna?
A. To increase the power handling capacity of a whip antenna
B. To reduce radiation resistance
C. To electrically lengthen a physically short antenna
D. To lower the radiation angle
        """
G4E02 = """
G4E02. What is the purpose of a corona ball on an HF mobile antenna?
A. To narrow the operating bandwidth of the antenna
B. To increase the “Q” of the antenna
C. To reduce the chance of damage if the antenna should strike an object
D. To reduce RF voltage discharge from the tip of the antenna while transmitting
        """
G4E03 = """
G4E03. Which of the following direct, fused power connections would be the best for a 100-watt HF mobile installation?
A. To the battery using heavy-gauge wire
B. To the alternator or generator using heavy-gauge wire
C. To the battery using insulated heavy duty balanced transmission line
D. To the alternator or generator using insulated heavy duty balanced transmission line
        """
G4E04 = """
G4E04. Why should DC power for a 100-watt HF transceiver not be supplied by a vehicle’s auxiliary power socket?
A. The socket is not wired with an RF-shielded power cable
B. The socket's wiring may be inadequate for the current drawn by the transceiver
C. The DC polarity of the socket is reversed from the polarity of modern HF transceivers
D. Drawing more than 50 watts from this socket could cause the engine to overheat
        """
G4E05 = """
G4E05. Which of the following most limits an HF mobile installation?
A. “Picket fencing”
B. The wire gauge of the DC power line to the transceiver
C. Efficiency of the electrically short antenna
D. FCC rules limiting mobile output power on the 75-meter band
        """
G4E06 = """
G4E06. What is one disadvantage of using a shortened mobile antenna as opposed to a full-size antenna?
A. Short antennas are more likely to cause distortion of transmitted signals
B. Q of the antenna will be very low
C. Operating bandwidth may be very limited
D. Harmonic radiation may increase
        """
G4E07 = """
G4E07. Which of the following may cause receive interference to an HF transceiver installed in a vehicle?
A. The battery charging system
B. The fuel delivery system
C. The control computers
D. All these choices are correct
        """
G4E08 = """
G4E08. In what configuration are the individual cells in a solar panel connected together?
A. Series-parallel
B. Shunt
C. Bypass
D. Full-wave bridge
        """
G4E09 = """
G4E09. What is the approximate open-circuit voltage from a fully illuminated silicon photovoltaic cell?
A. 0.02 VDC
B. 0.5 VDC
C. 0.2 VDC
D. 1.38 VDC
        """
G4E10 = """
G4E10. Why should a series diode be connected between a solar panel and a storage battery that is being charged by the panel?
A. To prevent overload by regulating the charging voltage
B. To prevent discharge of the battery through the panel during times of low or no illumination
C. To limit the current flowing from the panel to a safe value
D. To prevent damage to the battery due to excessive voltage at high illumination levels
        """
G4E11 = """
G4E11. What precaution should be taken when connecting a solar panel to a lithium iron phosphate battery?
A. Ground the solar panel outer metal framework
B. Ensure the battery is placed terminals-up
C. A series resistor must be in place
D. The solar panel must have a charge controller
        """



G5A01 = """
G5A01. What happens when inductive and capacitive reactance are equal in a series LC circuit?
A. Resonance causes impedance to be very high
B. Impedance is equal to the geometric mean of the inductance and capacitance
C. Resonance causes impedance to be very low
D. Impedance is equal to the arithmetic mean of the inductance and capacitance
        """
G5A02 = """
G5A02. What is reactance?
A. Opposition to the flow of direct current caused by resistance
B. Opposition to the flow of alternating current caused by capacitance or inductance
C. Reinforcement of the flow of direct current caused by resistance
D. Reinforcement of the flow of alternating current caused by capacitance or inductance
        """
G5A03 = """
G5A03. Which of the following is opposition to the flow of alternating current in an inductor?
A. Conductance
B. Reluctance
C. Admittance
D. Reactance
        """
G5A04 = """
G5A04. Which of the following is opposition to the flow of alternating current in a capacitor?
A. Conductance
B. Reluctance
C. Reactance
D. Admittance
        """
G5A05 = """
G5A05. How does an inductor react to AC?
A. As the frequency of the applied AC increases, the reactance decreases
B. As the amplitude of the applied AC increases, the reactance increases
C. As the amplitude of the applied AC increases, the reactance decreases
D. As the frequency of the applied AC increases, the reactance increases
        """
G5A06 = """
G5A06. How does a capacitor react to AC?
A. As the frequency of the applied AC increases, the reactance decreases
B. As the frequency of the applied AC increases, the reactance increases
C. As the amplitude of the applied AC increases, the reactance increases
D. As the amplitude of the applied AC increases, the reactance decreases
        """
G5A07 = """
G5A07. What is the term for the inverse of impedance?
A. Conductance
B. Susceptance
C. Reluctance
D. Admittance
        """
G5A08 = """
G5A08. What is impedance?
A. The ratio of current to voltage
B. The product of current and voltage
C. The ratio of voltage to current
D. The product of current and reactance 
        """
G5A09 = """
G5A09. What unit is used to measure reactance?
A. Farad
B. Ohm
C. Ampere
D. Siemens
        """
G5A10 = """
G5A10. Which of the following devices can be used for impedance matching at radio frequencies?
A. A transformer
B. A Pi-network
C. A length of transmission line
D. All these choices are correct
        """
G5A11 = """
G5A11. What letter is used to represent reactance?
A. Z
B. X
C. B
D. Y
        """
G5A12 = """
G5A12. What occurs in an LC circuit at resonance? 
A. Current and voltage are equal
B. Resistance is cancelled
C. The circuit radiates all its energy in the form of radio waves
D. Inductive reactance and capacitive reactance cancel
        """

G5B01 = """
G5B01. What dB change represents a factor of two increase or decrease in power?
A. Approximately 2 dB
B. Approximately 3 dB
C. Approximately 6 dB
D. Approximately 9 dB
        """
G5B02 = """
G5B02. How does the total current relate to the individual currents in a circuit of parallel resistors?
A. It equals the average of the branch currents
B. It decreases as more parallel branches are added to the circuit
C. It equals the sum of the currents through each branch
D. It is the sum of the reciprocal of each individual voltage drop
        """
G5B03 = """
G5B03. How many watts of electrical power are consumed if 400 VDC is supplied to an 800-ohm load?
A. 0.5 watts
B. 200 watts
C. 400 watts
D. 3200 watts
        """
G5B04 = """
G5B04. How many watts of electrical power are consumed by a 12 VDC light bulb that draws 0.2 amperes?
A. 2.4 watts
B. 24 watts
C. 6 watts
D. 60 watts
        """
G5B05 = """
G5B05. How many watts are consumed when a current of 7.0 milliamperes flows through a 1,250-ohm resistance?
A. Approximately 61 milliwatts
B. Approximately 61 watts
C. Approximately 11 milliwatts
D. Approximately 11 watts
        """
G5B06 = """
G5B06. What is the PEP produced by 200 volts peak-to-peak across a 50-ohm dummy load?
A. 1.4 watts
B. 100 watts
C. 353.5 watts
D. 400 watts
        """
G5B07 = """
G5B07. What value of an AC signal produces the same power dissipation in a resistor as a DC voltage of the same value?
A. The peak-to-peak value
B. The peak value
C. The RMS value
D. The reciprocal of the RMS value
        """
G5B08 = """
G5B08. What is the peak-to-peak voltage of a sine wave with an RMS voltage of 120 volts?
A. 84.8 volts
B. 169.7 volts
C. 240.0 volts
D. 339.4 volts
        """
G5B09 = """
G5B09. What is the RMS voltage of a sine wave with a value of 17 volts peak?
A. 8.5 volts
B. 12 volts
C. 24 volts
D. 34 volts
        """
G5B10 = """
G5B10. What percentage of power loss is equivalent to a loss of 1 dB?
A. 10.9 percent
B. 12.2 percent
C. 20.6 percent
D. 25.9 percent
        """
G5B11 = """
G5B11. What is the ratio of PEP to average power for an unmodulated carrier?
A. 0.707
B. 1.00
C. 1.414
D. 2.00
        """
G5B12 = """
G5B12. What is the RMS voltage across a 50-ohm dummy load dissipating 1200 watts?
A. 173 volts
B. 245 volts
C. 346 volts
D. 692 volts
        """
G5B13 = """
G5B13. What is the output PEP of an unmodulated carrier if the average power is 1060 watts?
A. 530 watts
B. 1060 watts
C. 1500 watts
D. 2120 watts
        """
G5B14 = """
G5B14. What is the output PEP of 500 volts peak-to-peak across a 50-ohm load?
A. 8.75 watts
B. 625 watts
C. 2500 watts
D. 5000 watts
        """


G5C01 = """
G5C01. What causes a voltage to appear across the secondary winding of a transformer when an AC voltage source is connected across its primary winding?
A. Capacitive coupling
B. Displacement current coupling
C. Mutual inductance
D. Mutual capacitance
        """
G5C02 = """
G5C02. What is the output voltage if an input signal is applied to the secondary winding of a 4:1 voltage step-down transformer instead of the primary winding?
A. The input voltage is multiplied by 4
B. The input voltage is divided by 4
C. Additional resistance must be added in series with the primary to prevent overload
D. Additional resistance must be added in parallel with the secondary to prevent overload
        """
G5C03 = """
G5C03. What is the total resistance of a 10-, a 20-, and a 50-ohm resistor connected in parallel?
A. 5.9 ohms
B. 0.17 ohms
C. 17 ohms
D. 80 ohms
        """
G5C04 = """
G5C04. What is the approximate total resistance of a 100- and a 200-ohm resistor in parallel?
A. 300 ohms
B. 150 ohms
C. 75 ohms
D. 67 ohms
        """
G5C05 = """
G5C05. Why is the primary winding wire of a voltage step-up transformer usually a larger size than that of the secondary winding?
A. To improve the coupling between the primary and secondary
B. To accommodate the higher current of the primary
C. To prevent parasitic oscillations due to resistive losses in the primary
D. To ensure that the volume of the primary winding is equal to the volume of the secondary winding
        """
G5C06 = """
G5C06. What is the voltage output of a transformer with a 500-turn primary and a 1500-turn secondary when 120 VAC is applied to the primary?
A. 360 volts
B. 120 volts
C. 40 volts
D. 25.5 volts 
        """
G5C06 = """
G5C07. What transformer turns ratio matches an antenna’s 600-ohm feed point impedance to a 50-ohm coaxial cable?
A. 3.5 to 1
B. 12 to 1
C. 24 to 1
D. 144 to 1
        """
G5C08 = """
G5C08. What is the equivalent capacitance of two 5.0-nanofarad capacitors and one 750-picofarad capacitor connected in parallel?
A. 576.9 nanofarads
B. 1,733 picofarads
C. 3,583 picofarads
D. 10.750 nanofarads
        """
G5C09 = """
G5C09. What is the capacitance of three 100-microfarad capacitors connected in series?
A. 0.33 microfarads
B. 3.0 microfarads
C. 33.3 microfarads
D. 300 microfarads
        """
G5C10 = """
G5C10. What is the inductance of three 10-millihenry inductors connected in parallel?
A. 0.30 henries
B. 3.3 henries
C. 3.3 millihenries
D. 30 millihenries
        """
G5C11 = """
G5C11. What is the inductance of a circuit with a 20-millihenry inductor connected in series with a 50-millihenry inductor?
A. 7 millihenries
B. 14.3 millihenries
C. 70 millihenries
D. 1,000 millihenries
        """
G5C12 = """
G5C12. What is the capacitance of a 20-microfarad capacitor connected in series with a 50-microfarad capacitor?
A. 0.07 microfarads
B. 14.3 microfarads
C. 70 microfarads
D. 1,000 microfarads
        """
G5C13 = """
G5C13. Which of the following components should be added to a capacitor to increase the capacitance?
A. An inductor in series
B. An inductor in parallel
C. A capacitor in parallel
D. A capacitor in series
        """
G5C14 = """
G5C14. Which of the following components should be added to an inductor to increase the inductance?
A. A capacitor in series
B. A capacitor in parallel
C. An inductor in parallel
D. An inductor in series
        """





G6A01 = """
G6A01. What is the minimum allowable discharge voltage for maximum life of a standard 12-volt lead-acid battery?
A. 6 volts
B. 8.5 volts
C. 10.5 volts
D. 12 volts
        """
G6A02 = """
G6A02. What is an advantage of batteries with low internal resistance?
A. Long life
B. High discharge current
C. High voltage
D. Rapid recharge
        """
G6A03 = """
G6A03. What is the approximate forward threshold voltage of a germanium diode?
A. 0.1 volt
B. 0.3 volts
C. 0.7 volts
D. 1.0 volts
        """
G6A04 = """
G6A04. Which of the following is characteristic of an electrolytic capacitor?
A. Tight tolerance
B. Much less leakage than any other type
C. High capacitance for a given volume
D. Inexpensive RF capacitor
        """
G6A05 = """
G6A05. What is the approximate forward threshold voltage of a silicon junction diode?
A. 0.1 volt
B. 0.3 volts
C. 0.7 volts
D. 1.0 volts
        """
G6A06 = """
G6A06. Why should wire-wound resistors not be used in RF circuits?
A. The resistor’s tolerance value would not be adequate
B. The resistor’s inductance could make circuit performance unpredictable
C. The resistor could overheat
D. The resistor’s internal capacitance would detune the circuit
        """
G6A07 = """
G6A07. What are the operating points for a bipolar transistor used as a switch?
A. Saturation and cutoff
B. The active region (between cutoff and saturation)
C. Peak and valley current points
D. Enhancement and depletion modes
        """
G6A08 = """
G6A08. Which of the following is characteristic of low voltage ceramic capacitors?
A. Tight tolerance
B. High stability
C. High capacitance for given volume
D. Comparatively low cost
        """
G6A09 = """
G6A09. Which of the following describes MOSFET construction?
A. The gate is formed by a back-biased junction
B. The gate is separated from the channel by a thin insulating layer
C. The source is separated from the drain by a thin insulating layer
D. The source is formed by depositing metal on silicon
        """
G6A10 = """
G6A10. Which element of a vacuum tube regulates the flow of electrons between cathode and plate?
A. Control grid
B. Suppressor grid
C. Screen grid
D. Trigger electrode
        """
G6A11 = """
G6A11. What happens when an inductor is operated above its self-resonant frequency?
A. Its reactance increases
B. Harmonics are generated
C. It becomes capacitive
D. Catastrophic failure is likely
        """
G6A12 = """
G6A12. What is the primary purpose of a screen grid in a vacuum tube?
A. To reduce grid-to-plate capacitance
B. To increase efficiency
C. To increase the control grid resistance
D. To decrease plate resistance
        """


G6B01 = """
G6B01. What determines the performance of a ferrite core at different frequencies?
A. Its conductivity
B. Its thickness
C. The composition, or “mix,” of materials used
D. The ratio of outer diameter to inner diameter
        """
G6B02 = """
G6B02. What is meant by the term MMIC?
A. Multi-Mode Integrated Circuit
B. Monolithic Microwave Integrated Circuit
C. Metal Monolayer Integrated Circuit
D. Mode Modulated Integrated Circuit
        """
G6B03 = """
G6B03. Which of the following is an advantage of CMOS integrated circuits compared to TTL integrated circuits?
A. Low power consumption
B. High power handling capability
C. Better suited for RF amplification
D. Better suited for power supply regulation
        """
G6B04 = """
G6B04. What is a typical upper frequency limit for low SWR operation of 50-ohm BNC connectors?
A. 50 MHz
B. 500 MHz
C. 4 GHz
D. 40 GHz
        """
G6B05 = """
G6B05. What is an advantage of using a ferrite core toroidal inductor?
A. Large values of inductance may be obtained
B. The magnetic properties of the core may be optimized for a specific range of frequencies
C. Most of the magnetic field is contained in the core
D. All these choices are correct
        """
G6B06 = """
G6B06. What kind of device is an integrated circuit operational amplifier?
A. Digital
B. MMIC
C. Programmable Logic
D. Analog
        """
G6B07 = """
G6B07. Which of the following describes a type N connector?
A. A moisture-resistant RF connector useful to 10 GHz
B. A small bayonet connector used for data circuits
C. A low noise figure VHF connector
D. A nickel plated version of the PL-259
        """
G6B08 = """
G6B08. How is an LED biased when emitting light?
A. In the tunnel-effect region
B. At the Zener voltage
C. Reverse biased
D. Forward biased
        """


G6B10 = """
G6B10. How does a ferrite bead or core reduce common-mode RF current on the shield of a coaxial cable?
A. By creating an impedance in the current’s path
B. It converts common-mode current to differential mode current
C. By creating an out-of-phase current to cancel the common-mode current
D. Ferrites expel magnetic fields
        """
G6B11 = """
G6B11. What is an SMA connector?
A. A type-S to type-M adaptor
B. A small threaded connector suitable for signals up to several GHz
C. A connector designed for serial multiple access signals
D. A type of push-on connector intended for high-voltage applications
        """
G6B12 = """
G6B12. Which of these connector types is commonly used for low frequency or dc signal connections to a transceiver?
A. PL-259
B. BNC
C. RCA Phono
D. Type N
        """




G7A01 = """
G7A01. What is the function of a power supply bleeder resistor?
A. It acts as a fuse for excess voltage
B. It discharges the filter capacitors when power is removed
C. It removes shock hazards from the induction coils
D. It eliminates ground loop current
        """
G7A02 = """
G7A02. Which of the following components are used in a power supply filter network?
A. Diodes
B. Transformers and transducers
C. Capacitors and inductors
D. All these choices are correct
        """
G7A03 = """
G7A03. Which type of rectifier circuit uses two diodes and a center-tapped transformer?
A. Full-wave
B. Full-wave bridge
C. Half-wave
D. Synchronous
        """
G7A04 = """
G7A04. What is characteristic of a half-wave rectifier in a power supply?
A. Only one diode is required
B. The ripple frequency is twice that of a full-wave rectifier
C. More current can be drawn from the half-wave rectifier
D. The output voltage is two times the peak input voltage
        """
G7A05 = """
G7A05. What portion of the AC cycle is converted to DC by a half-wave rectifier?
A. 90 degrees
B. 180 degrees
C. 270 degrees
D. 360 degrees
        """
G7A06 = """
G7A06. What portion of the AC cycle is converted to DC by a full-wave rectifier?
A. 90 degrees
B. 180 degrees
C. 270 degrees
D. 360 degrees
        """
G7A07 = """
G7A07. What is the output waveform of an unfiltered full-wave rectifier connected to a resistive load?
A. A series of DC pulses at twice the frequency of the AC input
B. A series of DC pulses at the same frequency as the AC input
C. A sine wave at half the frequency of the AC input
D. A steady DC voltage
        """
G7A08 = """
G7A08. Which of the following is characteristic of a switchmode power supply as compared to a linear power supply?
A. Faster switching time makes higher output voltage possible
B. Fewer circuit components are required
C. High-frequency operation allows the use of smaller components
D. Inherently more stable
        """


G7B01 = """
G7B01. What is the purpose of neutralizing an amplifier?
A. To limit the modulation index
B. To eliminate self-oscillations
C. To cut off the final amplifier during standby periods
D. To keep the carrier on frequency
        """
G7B02 = """
G7B02. Which of these classes of amplifiers has the highest efficiency?
A. Class A
B. Class B
C. Class AB
D. Class C
        """
G7B03 = """
G7B03. Which of the following describes the function of a two-input AND gate?
A. Output is high when either or both inputs are low
B. Output is high only when both inputs are high
C. Output is low when either or both inputs are high
D. Output is low only when both inputs are high
        """
G7B04 = """
G7B04. In a Class A amplifier, what percentage of the time does the amplifying device conduct?
A. 100%
B. More than 50% but less than 100%
C. 50%
D. Less than 50%
        """
G7B05 = """
G7B05. How many states does a 3-bit binary counter have?
A. 3
B. 6
C. 8
D. 16
        """
G7B06 = """
G7B06. What is a shift register?
A. A clocked array of circuits that passes data in steps along the array
B. An array of operational amplifiers used for tri-state arithmetic operations
C. A digital mixer
D. An analog mixer
        """
G7B07 = """
G7B07. Which of the following are basic components of a sine wave oscillator?
A. An amplifier and a divider
B. A frequency multiplier and a mixer
C. A circulator and a filter operating in a feed-forward loop
D. A filter and an amplifier operating in a feedback loop
        """
G7B08 = """
G7B08. How is the efficiency of an RF power amplifier determined?
A. Divide the DC input power by the DC output power
B. Divide the RF output power by the DC input power
C. Multiply the RF input power by the reciprocal of the RF output power
D. Add the RF input power to the DC output power
        """
G7B09 = """
G7B09. What determines the frequency of an LC oscillator?
A. The number of stages in the counter
B. The number of stages in the divider
C. The inductance and capacitance in the tank circuit
D. The time delay of the lag circuit
        """
G7B10 = """
G7B10. Which of the following describes a linear amplifier?
A. Any RF power amplifier used in conjunction with an amateur transceiver
B. An amplifier in which the output preserves the input waveform
C. A Class C high efficiency amplifier
D. An amplifier used as a frequency multiplier
        """
G7B11 = """
G7B11. For which of the following modes is a Class C power stage appropriate for amplifying a modulated signal?
A. SSB
B. FM
C. AM
D. All these choices are correct
        """

G7C01 = """
G7C01. What circuit is used to select one of the sidebands from a balanced modulator?
A. Carrier oscillator
B. Filter
C. IF amplifier
D. RF amplifier
        """
G7C02 = """
G7C02. What output is produced by a balanced modulator?
A. Frequency modulated RF
B. Audio with equalized frequency response
C. Audio extracted from the modulation signal
D. Double-sideband modulated RF
        """
G7C03 = """
G7C03. What is one reason to use an impedance matching transformer at a transmitter output?
A. To minimize transmitter power output
B. To present the desired impedance to the transmitter and feed line
C. To reduce power supply ripple
D. To minimize radiation resistance
        """
G7C04 = """
G7C04. How is a product detector used?
A. Used in test gear to detect spurious mixing products
B. Used in transmitter to perform frequency multiplication
C. Used in an FM receiver to filter out unwanted sidebands
D. Used in a single sideband receiver to extract the modulated signal
        """
G7C05 = """
G7C05. Which of the following is characteristic of a direct digital synthesizer (DDS)?
A. Extremely narrow tuning range
B. Relatively high-power output
C. Pure sine wave output
D. Variable output frequency with the stability of a crystal oscillator
        """
G7C06 = """
G7C06. Which of the following is an advantage of a digital signal processing (DSP) filter compared to an analog filter?
A. A wide range of filter bandwidths and shapes can be created
B. Fewer digital components are required
C. Mixing products are greatly reduced
D. The DSP filter is much more effective at VHF frequencies
        """
G7C07 = """
G7C07. What term specifies a filter’s attenuation inside its passband?
A. Insertion loss
B. Return loss
C. Q
D. Ultimate rejection
        """
G7C08 = """
G7C08. Which parameter affects receiver sensitivity?
A. Input amplifier gain
B. Demodulator stage bandwidth
C. Input amplifier noise figure
D. All these choices are correct
        """
G7C09 = """
G7C09. What is the phase difference between the I and Q RF signals that software-defined radio (SDR) equipment uses for modulation and demodulation?
A. Zero
B. 90 degrees
C. 180 degrees
D. 45 degrees
        """
G7C10 = """
G7C10. What is an advantage of using I-Q modulation with software-defined radios (SDRs)?
A. The need for high resolution analog-to-digital converters is eliminated
B. All types of modulation can be created with appropriate processing
C. Minimum detectible signal level is reduced
D. Automatic conversion of the signal from digital to analog
        """
G7C11 = """
G7C11. Which of these functions is performed by software in a software-defined radio (SDR)?
A. Filtering
B. Detection 
C. Modulation
D. All these choices are correct
        """
G7C12 = """
G7C12. What is the frequency above which a low-pass filter’s output power is less than half the input power?
A. Notch frequency
B. Neper frequency
C. Cutoff frequency
D. Rolloff frequency
        """
G7C13 = """
G7C13. What term specifies a filter’s maximum ability to reject signals outside its passband?
A. Notch depth
B. Rolloff
C. Insertion loss
D. Ultimate rejection
        """
G7C14 = """
G7C14. The bandwidth of a band-pass filter is measured between what two frequencies?
A. Upper and lower half-power
B. Cutoff and rolloff
C. Pole and zero
D. Image and harmonic
        """






G8A01 = """
G8A01. How is direct binary FSK modulation generated?
A. By keying an FM transmitter with a sub-audible tone
B. By changing an oscillator's frequency directly with a digital control signal
C. By using a transceiver's computer data interface protocol to change frequencies
D. By reconfiguring the CW keying input to act as a tone generator
        """
G8A02 = """
G8A02. What is the name of the process that changes the phase angle of an RF signal to convey information?
A. Phase convolution
B. Phase modulation
C. Phase transformation
D. Phase inversion
        """
G8A03 = """
G8A03. What is the name of the process that changes the instantaneous frequency of an RF wave to convey information?
A. Frequency convolution
B. Frequency transformation
C. Frequency conversion
D. Frequency modulation
        """
G8A04 = """
G8A04. What emission is produced by a reactance modulator connected to a transmitter RF amplifier stage?
A. Multiplex modulation
B. Phase modulation
C. Amplitude modulation
D. Pulse modulation
        """
G8A05 = """
G8A05. What type of modulation varies the instantaneous power level of the RF signal?
A. Power modulation
B. Phase modulation
C. Frequency modulation
D. Amplitude modulation
        """
G8A06 = """
G8A06. Which of the following is characteristic of QPSK31?
A. It is sideband sensitive
B. Its encoding provides error correction
C. Its bandwidth is approximately the same as BPSK31
D. All these choices are correct
        """
G8A07 = """
G8A07. Which of the following phone emissions uses the narrowest bandwidth?
A. Single sideband
B. Vestigial sideband
C. Phase modulation
D. Frequency modulation
        """
G8A08 = """
G8A08. Which of the following is an effect of overmodulation?
A. Insufficient audio
B. Insufficient bandwidth
C. Frequency drift
D. Excessive bandwidth
        """
G8A09 = """
G8A09. What type of modulation is used by FT8?
A. 8-tone frequency shift keying
B. Vestigial sideband
C. Amplitude compressed AM
D. 8-bit direct sequence spread spectrum
        """
G8A10 = """
G8A10. What is meant by the term “flat-topping,” when referring to an amplitude-modulated phone signal?
A. Signal distortion caused by insufficient collector current
B. The transmitter's automatic level control (ALC) is properly adjusted
C. Signal distortion caused by excessive drive or speech levels
D. The transmitter's carrier is properly suppressed
        """
G8A11 = """
G8A11. What is the modulation envelope of an AM signal?
A. The waveform created by connecting the peak values of the modulated signal
B. The carrier frequency that contains the signal
C. Spurious signals that envelop nearby frequencies
D. The bandwidth of the modulated signal
        """
G8A12 = """
G8A12. What is QPSK modulation?
A. Modulation using quasi-parallel to serial conversion to reduce bandwidth
B. Modulation using quadra-pole sideband keying to generate spread spectrum signals
C. Modulation using Fast Fourier Transforms to generate frequencies at the first, second, third, and fourth harmonics of the carrier frequency to improve noise immunity
D. Modulation in which digital data is transmitted using 0-, 90-, 180- and 270-degrees phase shift to represent pairs of bits
        """
G8A13 = """
G8A13. What is a link budget?
A. The financial costs associated with operating a radio link
B. The sum of antenna gains minus system losses
C. The sum of transmit power and antenna gains minus system losses as seen at the receiver
D. The difference between transmit power and receiver sensitivity
        """
G8A14 = """
G8A14. What is link margin?
A. The opposite of fade margin
B. The difference between received power level and minimum required signal level at the input to the receiver
C. Transmit power minus receiver sensitivity
D. Receiver sensitivity plus 3 dB
        """

G8B01 = """
G8B01. Which mixer input is varied or tuned to convert signals of different frequencies to an intermediate frequency (IF)?
A. Image frequency
B. Local oscillator
C. RF input
D. Beat frequency oscillator
        """
G8B02 = """
G8B02. What is the term for interference from a signal at twice the IF frequency from the desired signal?
A. Quadrature response
B. Image response
C. Mixer interference
D. Intermediate interference
        """
G8B03 = """
G8B03. What is another term for the mixing of two RF signals?
A. Heterodyning
B. Synthesizing
C. Frequency inversion
D. Phase inversion
        """
G8B04 = """
G8B04. What is the stage in a VHF FM transmitter that generates a harmonic of a lower frequency signal to reach the desired operating frequency?
A. Mixer
B. Reactance modulator
C. Balanced converter
D. Multiplier
        """
G8B05 = """
G8B05. Which intermodulation products are closest to the original signal frequencies?
A. Second harmonics
B. Even-order
C. Odd-order
D. Intercept point
        """
G8B06 = """
G8B06. What is the total bandwidth of an FM phone transmission having 5 kHz deviation and 3 kHz modulating frequency?
A. 3 kHz
B. 5 kHz
C. 8 kHz
D. 16 kHz
        """
G8B07 = """
G8B07. What is the frequency deviation for a 12.21 MHz reactance modulated oscillator in a 5 kHz deviation, 146.52 MHz FM phone transmitter?
A. 101.75 Hz
B. 416.7 Hz
C. 5 kHz
D. 60 kHz
        """
G8B08 = """
G8B08. Why is it important to know the duty cycle of the mode you are using when transmitting?
A. To aid in tuning your transmitter
B. Some modes have high duty cycles that could exceed the transmitter’s average power rating
C. To allow time for the other station to break in during a transmission
D. To prevent overmodulation
        """
G8B09 = """
G8B09. Why is it good to match receiver bandwidth to the bandwidth of the operating mode?
A. It is required by FCC rules
B. It minimizes power consumption in the receiver
C. It improves impedance matching of the antenna
D. It results in the best signal-to-noise ratio
        """
G8B10 = """
G8B10. What is the relationship between transmitted symbol rate and bandwidth?
A. Symbol rate and bandwidth are not related
B. Higher symbol rates require wider bandwidth
C. Lower symbol rates require wider bandwidth
D. Bandwidth is half the symbol rate
        """
G8B11 = """
G8B11. What combination of a mixer's Local Oscillator (LO) and RF input frequencies is found in the output?
A. The ratio
B. The average
C. The sum and difference
D. The arithmetic product
        """
G8B12 = """
G8B12. What process combines two signals in a non-linear circuit to produce unwanted spurious outputs?
A. Intermodulation
B. Heterodyning
C. Detection
D. Rolloff
        """
G8B13 = """
G8B13. Which of the following is an odd-order intermodulation product of frequencies F1 and F2?
A. 5F1-3F2
B. 3F1-F2
C. 2F1-F2
D. All these choices are correct
        """


G8C01 = """
G8C01. On what band do amateurs share channels with the unlicensed Wi-Fi service?
A. 432 MHz
B. 902 MHz
C. 2.4 GHz
D. 10.7 GHz
        """
G8C02 = """
G8C02. Which digital mode is used as a low-power beacon for assessing HF propagation?
A. WSPR
B. MFSK16
C. PSK31
D. SSB-SC
        """
G8C03 = """
G8C03. What part of a packet radio frame contains the routing and handling information?
A. Directory
B. Preamble
C. Header
D. Trailer
        """
G8C04 = """
G8C04. Which of the following describes Baudot code?
A. A 7-bit code with start, stop, and parity bits
B. A code using error detection and correction
C. A 5-bit code with additional start and stop bits
D. A code using SELCAL and LISTEN
        """
G8C05 = """
G8C05. In an ARQ mode, what is meant by a NAK response to a transmitted packet?
A. Request retransmission of the packet
B. Packet was received without error
C. Receiving station connected and ready for transmissions
D. Entire file received correctly
        """
G8C06 = """
G8C06. What action results from a failure to exchange information due to excessive transmission attempts when using an ARQ mode?
A. The checksum overflows
B. The connection is dropped
C. Packets will be routed incorrectly
D. Encoding reverts to the default character set
        """
G8C07 = """
G8C07. Which of the following narrow-band digital modes can receive signals with very low signal-to-noise ratios?
A. MSK144
B. FT8
C. AMTOR
D. MFSK32
        """
G8C08 = """
G8C08. Which of the following statements is true about PSK31?
A. Upper case letters are sent with more power
B. Upper case letters use longer Varicode bit sequences and thus slow down transmission
C. Error correction is used to ensure accurate message reception
D. Higher power is needed as compared to RTTY for similar error rates
        """
G8C09 = """
G8C09. Which is true of mesh network microwave nodes?
A. Having more nodes increases signal strengths
B. If one node fails, a packet may still reach its target station via an alternate node
C. Links between two nodes in a network may have different frequencies and bandwidths
D. More nodes reduce overall microwave out of band interference
        """
G8C10 = """
G8C10. How does forward error correction (FEC) allow the receiver to correct data errors?
A. By controlling transmitter output power for optimum signal strength
B. By using the Varicode character set
C. By transmitting redundant information with the data
D. By using a parity bit with each character
        """
G8C11 = """
G8C11. How are the two separate frequencies of a Frequency Shift Keyed (FSK) signal identified?
A. Dot and dash
B. On and off
C. High and low
D. Mark and space
        """
G8C12 = """
G8C12. Which type of code is used for sending characters in a PSK31 signal?
A. Varicode
B. Viterbi
C. Volumetric
D. Binary
        """
G8C13 = """
G8C13. What is indicated on a waterfall display by one or more vertical lines on either side of a data mode or RTTY signal?
A. Long path propagation
B. Backscatter propagation
C. Insufficient modulation
D. Overmodulation
        """
G8C14 = """
G8C14. Which of the following describes a waterfall display?
A. Frequency is horizontal, signal strength is vertical, time is intensity
B. Frequency is vertical, signal strength is intensity, time is horizontal
C. Frequency is horizontal, signal strength is intensity, time is vertical
D. Frequency is vertical, signal strength is horizontal, time is intensity
        """
G8C15 = """
G8C15. What does an FT8 signal report of +3 mean?
A. The signal is 3 times the noise level of an equivalent SSB signal
B. The signal is S3 (weak signals)
C. The signal-to-noise ratio is equivalent to +3dB in a 2.5 kHz bandwidth
D. The signal is 3 dB over S9
        """
G8C16 = """
G8C16. Which of the following provide digital voice modes?
A. WSPR, MFSK16, and EasyPAL
B. FT8, FT4, and FST4
C. Winlink, PACTOR II, and PACTOR III
D. DMR, D-STAR, and SystemFusion
        """




G9A01 = """
G9A01. Which of the following factors determine the characteristic impedance of a parallel conductor feed line?
A. The distance between the centers of the conductors and the radius of the conductors
B. The distance between the centers of the conductors and the length of the line
C. The radius of the conductors and the frequency of the signal
D. The frequency of the signal and the length of the line
        """
G9A02 = """
G9A02. What is the relationship between high standing wave ratio (SWR) and transmission line loss?
A. There is no relationship between transmission line loss and SWR
B. High SWR increases loss in a lossy transmission line
C. High SWR makes it difficult to measure transmission line loss
D. High SWR reduces the relative effect of transmission line loss
        """
G9A03 = """
G9A03. What is the nominal characteristic impedance of “window line” transmission line?
A. 50 ohms
B. 75 ohms
C. 100 ohms
D. 450 ohms
        """
G9A04 = """
G9A04. What causes reflected power at an antenna’s feed point?
A. Operating an antenna at its resonant frequency
B. Using more transmitter power than the antenna can handle
C. A difference between feed line impedance and antenna feed point impedance
D. Feeding the antenna with unbalanced feed line
        """
G9A05 = """
G9A05. How does the attenuation of coaxial cable change with increasing frequency?
A. Attenuation is independent of frequency
B. Attenuation increases
C. Attenuation decreases
D. Attenuation follows Marconi's Law of Attenuation
        """
G9A06 = """
G9A06. In what units is RF feed line loss usually expressed?
A. Ohms per 1,000 feet
B. Decibels per 1,000 feet
C. Ohms per 100 feet
D. Decibels per 100 feet
        """
G9A07 = """
G9A07. What must be done to prevent standing waves on a feed line connected to an antenna?
A. The antenna feed point must be at DC ground potential
B. The feed line must be an odd number of electrical quarter wavelengths long
C. The feed line must be an even number of physical half wavelengths long
D. The antenna feed point impedance must be matched to the characteristic impedance of the feed line
        """
G9A08 = """
G9A08. If the SWR on an antenna feed line is 5:1, and a matching network at the transmitter end of the feed line is adjusted to present a 1:1 SWR to the transmitter, what is the resulting SWR on the feed line?
A. 1:1
B. 5:1
C. Between 1:1 and 5:1 depending on the characteristic impedance of the line
D. Between 1:1 and 5:1 depending on the reflected power at the transmitter
        """
G9A09 = """
G9A09. What standing wave ratio results from connecting a 50-ohm feed line to a 200-ohm resistive load?
A. 4:1
B. 1:4
C. 2:1
D. 1:2
        """
G9A10 = """
G9A10. What standing wave ratio results from connecting a 50-ohm feed line to a 10-ohm resistive load?
A. 2:1
B. 1:2
C. 1:5
D. 5:1
        """
G9A11 = """
G9A11. What is the effect of transmission line loss on SWR measured at the input to the line?
A. Higher loss reduces SWR measured at the input to the line
B. Higher loss increases SWR measured at the input to the line
C. Higher loss increases the accuracy of SWR measured at the input to the line
D. Transmission line loss does not affect the SWR measurement
        """


G9B01 = """
G9B01. What is a characteristic of a random-wire HF antenna connected directly to the transmitter?
A. It must be longer than 1 wavelength
B. Station equipment may carry significant RF current
C. It produces only vertically polarized radiation
D. It is more effective on the lower HF bands than on the higher bands
        """
G9B02 = """
G9B02. Which of the following is a common way to adjust the feed point impedance of an elevated quarter-wave ground-plane vertical antenna to be approximately 50 ohms?
A. Slope the radials upward
B. Slope the radials downward
C. Lengthen the radials beyond one wavelength
D. Coil the radials
        """
G9B03 = """
G9B03. Which of the following best describes the radiation pattern of a quarter-wave ground-plane vertical antenna?
A. Bi-directional in azimuth
B. Isotropic
C. Hemispherical
D. Omnidirectional in azimuth
        """
G9B04 = """
G9B04. What is the radiation pattern of a dipole antenna in free space in a plane containing the conductor?
A. It is a figure-eight at right angles to the antenna
B. It is a figure-eight off both ends of the antenna
C. It is a circle (equal radiation in all directions)
D. It has a pair of lobes on one side of the antenna and a single lobe on the other side
        """
G9B05 = """
G9B05. How does antenna height affect the azimuthal radiation pattern of a horizontal dipole HF antenna at elevation angles higher than about 45 degrees?
A. If the antenna is too high, the pattern becomes unpredictable
B. Antenna height has no effect on the pattern
C. If the antenna is less than 1/2 wavelength high, the azimuthal pattern is almost omnidirectional
D. If the antenna is less than 1/2 wavelength high, radiation off the ends of the wire is eliminated
        """
G9B06 = """
G9B06. Where should the radial wires of a ground-mounted vertical antenna system be placed?
A. As high as possible above the ground
B. Parallel to the antenna element
C. On the surface or buried a few inches below the ground
D. At the center of the antenna
        """
G9B07 = """
G9B07. How does the feed point impedance of a horizontal 1/2 wave dipole antenna change as the antenna height is reduced to 1/10 wavelength above ground?
A. It steadily increases
B. It steadily decreases
C. It peaks at about 1/8 wavelength above ground
D. It is unaffected by the height above ground
        """
G9B08 = """
G9B08. How does the feed point impedance of a 1/2 wave dipole change as the feed point is moved from the center toward the ends?
A. It steadily increases
B. It steadily decreases
C. It peaks at about 1/8 wavelength from the end
D. It is unaffected by the location of the feed point
        """
G9B09 = """
G9B09. Which of the following is an advantage of using a horizontally polarized as compared to a vertically polarized HF antenna?
A. Lower ground losses
B. Lower feed point impedance
C. Shorter radials
D. Lower radiation resistance
        """
G9B10 = """
G9B10. What is the approximate length for a 1/2 wave dipole antenna cut for 14.250 MHz?
A. 8 feet
B. 16 feet
C. 24 feet
D. 33 feet
        """
G9B11 = """
G9B11. What is the approximate length for a 1/2 wave dipole antenna cut for 3.550 MHz?
A. 42 feet
B. 84 feet
C. 132 feet
D. 263 feet
        """
G9B12 = """
G9B12. What is the approximate length for a 1/4 wave monopole antenna cut for 28.5 MHz?
A. 8 feet
B. 11 feet
C. 16 feet
D. 21 feet
        """


G9C01 = """
G9C01. Which of the following would increase the bandwidth of a Yagi antenna?
A. Larger-diameter elements
B. Closer element spacing
C. Loading coils in series with the element
D. Tapered-diameter elements
        """
G9C02 = """
G9C02. What is the approximate length of the driven element of a Yagi antenna?
A. 1/4 wavelength
B. 1/2 wavelength
C. 3/4 wavelength
D. 1 wavelength
        """
G9C03 = """
G9C03. How do the lengths of a three-element Yagi reflector and director compare to that of the driven element?
A. The reflector is longer, and the director is shorter
B. The reflector is shorter, and the director is longer
C. They are all the same length
D. Relative length depends on the frequency of operation
        """
G9C04 = """
G9C04. How does antenna gain in dBi compare to gain stated in dBd for the same antenna?
A. Gain in dBi is 2.15 dB lower
B. Gain in dBi is 2.15 dB higher
C. Gain in dBd is 1.25 dBd lower
D. Gain in dBd is 1.25 dBd higher
        """
G9C05 = """
G9C05. What is the primary effect of increasing boom length and adding directors to a Yagi antenna?
A. Gain increases
B. Beamwidth increases
C. Front-to-back ratio decreases
D. Resonant frequency is lower
        """
G9C07 = """
G9C07. What does “front-to-back ratio” mean in reference to a Yagi antenna?
A. The number of directors versus the number of reflectors
B. The relative position of the driven element with respect to the reflectors and directors
C. The power radiated in the major lobe compared to that in the opposite direction
D. The ratio of forward gain to dipole gain
        """
G9C08 = """
G9C08. What is meant by the “main lobe” of a directive antenna?
A. The magnitude of the maximum vertical angle of radiation
B. The point of maximum current in a radiating antenna element
C. The maximum voltage standing wave point on a radiating element
D. The direction of maximum radiated field strength from the antenna
        """
G9C09 = """
G9C09. In free space, how does the gain of two three-element, horizontally polarized Yagi antennas spaced vertically 1/2 wavelength apart typically compare to the gain of a single three-element Yagi?
A. Approximately 1.5 dB higher
B. Approximately 3 dB higher
C. Approximately 6 dB higher
D. Approximately 9 dB higher
        """
G9C10 = """
G9C10. Which of the following can be adjusted to optimize forward gain, front-to-back ratio, or SWR bandwidth of a Yagi antenna?
A. The physical length of the boom
B. The number of elements on the boom
C. The spacing of each element along the boom
D. All these choices are correct
        """
G9C11 = """
G9C11. What is a beta or hairpin match?
A. A shorted transmission line stub placed at the feed point of a Yagi antenna to provide impedance matching
B. A 1/4 wavelength section of 75-ohm coax in series with the feed point of a Yagi to provide impedance matching
C. A series capacitor selected to cancel the inductive reactance of a folded dipole antenna
D. A section of 300-ohm twin-lead transmission line used to match a folded dipole antenna
        """
G8C12 = """
G9C12. Which of the following is a characteristic of using a gamma match with a Yagi antenna?
A. It does not require the driven element to be insulated from the boom
B. It does not require any inductors or capacitors
C. It is useful for matching multiband antennas
D. All these choices are correct
        """


G9D01 = """
G9D01. Which of the following antenna types will be most effective as a near vertical incidence skywave (NVIS) antenna for short-skip communications on 40 meters during the day?
A. A horizontal dipole placed between 1/10 and 1/4 wavelength above the ground
B. A vertical antenna placed between 1/4 and 1/2 wavelength above the ground
C. A horizontal dipole placed at approximately 1/2 wavelength above the ground
D. A vertical dipole placed at approximately 1/2 wavelength above the ground
        """
G9D02 = """
G9D02. What is the feed point impedance of an end-fed half-wave antenna?
A. Very low
B. Approximately 50 ohms
C. Approximately 300 ohms
D. Very high
        """
G9D03 = """
G9D03. In which direction is the maximum radiation from a VHF/UHF “halo” antenna?
A. Broadside to the plane of the halo
B. Opposite the feed point
C. Omnidirectional in the plane of the halo
D. On the same side as the feed point
        """
G9D04 = """
G9D04. What is the primary function of antenna traps?
A. To enable multiband operation
B. To notch spurious frequencies
C. To provide balanced feed point impedance
D. To prevent out-of-band operation
        """
G9D05 = """
G9D05. What is an advantage of vertically stacking horizontally polarized Yagi antennas?
A. It allows quick selection of vertical or horizontal polarization
B. It allows simultaneous vertical and horizontal polarization
C. It narrows the main lobe in azimuth
D. It narrows the main lobe in elevation
        """
G9D06 = """
G9D06. Which of the following is an advantage of a log-periodic antenna?
A. Wide bandwidth
B. Higher gain per element than a Yagi antenna
C. Harmonic suppression
D. Polarization diversity
        """
G9D07 = """
G9D07. Which of the following describes a log-periodic antenna?
A. Element length and spacing vary logarithmically along the boom
B. Impedance varies periodically as a function of frequency
C. Gain varies logarithmically as a function of frequency
D. SWR varies periodically as a function of boom length
        """
G9D08 = """
G9D08. How does a “screwdriver” mobile antenna adjust its feed point impedance?
A. By varying its body capacitance
B. By varying the base loading inductance
C. By extending and retracting the whip
D. By deploying a capacitance hat
        """
G9D09 = """
G9D09. What is the primary use of a Beverage antenna?
A. Directional receiving for MF and low HF bands
B. Directional transmitting for low HF bands
C. Portable direction finding at higher HF frequencies
D. Portable direction finding at lower HF frequencies
        """
G9D10 = """
G9D10. In which direction or directions does an electrically small loop (less than 1/10 wavelength in circumference) have nulls in its radiation pattern?
A. In the plane of the loop
B. Broadside to the loop
C. Broadside and in the plane of the loop
D. Electrically small loops are omnidirectional
        """
G9D11 = """
G9D11. Which of the following is a disadvantage of multiband antennas?
A. They present low impedance on all design frequencies
B. They must be used with an antenna tuner
C. They must be fed with open wire line
D. They have poor harmonic rejection
        """
G9D12 = """
G9D12. What is the common name of a dipole with a single central support?
A. Inverted V
B. Inverted L
C. Sloper
D. Lazy H
        """



G0A01 = """
G0A01. What is one way that RF energy can affect human body tissue?
A. It heats body tissue
B. It causes radiation poisoning
C. It causes the blood count to reach a dangerously low level
D. It cools body tissue
        """
G0A02 = """
G0A02. Which of the following is used to determine RF exposure from a transmitted signal?
A. Its duty cycle
B. Its frequency
C. Its power density
D. All these choices are correct
        """
G0A03 = """
G0A03. How can you determine that your station complies with FCC RF exposure regulations?
A. By calculation based on FCC OET Bulletin 65
B. By calculation based on computer modeling
C. By measurement of field strength using calibrated equipment
D. All these choices are correct
        """
G0A04 = """
G0A04. What does “time averaging” mean when evaluating RF radiation exposure?
A. The average amount of power developed by the transmitter over a specific 24-hour period
B. The average time it takes RF radiation to have any long-term effect on the body
C. The total time of the exposure
D. The total RF exposure averaged over a certain period
        """
G0A05 = """
G0A05. What must you do if an evaluation of your station shows that the RF energy radiated by your station exceeds permissible limits for possible human absorption?
A. Take action to prevent human exposure to the excessive RF fields
B. File an Environmental Impact Statement (EIS-97) with the FCC
C. Secure written permission from your neighbors to operate above the controlled MPE limits
D. All these choices are correct
        """
G0A06 = """
G0A06. What must you do if your station fails to meet the FCC RF exposure exemption criteria?
A. Perform an RF Exposure Evaluation in accordance with FCC OET Bulletin 65
B. Contact the FCC for permission to transmit
C. Perform an RF exposure evaluation in accordance with World Meteorological Organization guidelines
D. Use an FCC-approved band-pass filter
        """
G0A07 = """
G0A07. What is the effect of modulation duty cycle on RF exposure?
A. A lower duty cycle permits greater power levels to be transmitted
B. A higher duty cycle permits greater power levels to be transmitted
C. Low duty cycle transmitters are exempt from RF exposure evaluation requirements
D. High duty cycle transmitters are exempt from RF exposure requirements
        """
G0A08 = """
G0A08. Which of the following steps must an amateur operator take to ensure compliance with RF safety regulations?
A. Post a copy of FCC Part 97.13 in the station
B. Notify neighbors within a 100-foot radius of the antenna of the existence of the station and power levels
C. Perform a routine RF exposure evaluation and prevent access to any identified high exposure areas
D. All these choices are correct
        """
G0A09 = """
G0A09. What type of instrument can be used to accurately measure an RF field strength?
A. A receiver with digital signal processing (DSP) noise reduction
B. A calibrated field strength meter with a calibrated antenna
C. An SWR meter with a peak-reading function
D. An oscilloscope with a high-stability crystal marker generator
        """
G0A10 = """
G0A10. What should be done if evaluation shows that a neighbor might experience more than the allowable limit of RF exposure from the main lobe of a directional antenna?
A. Change to a non-polarized antenna with higher gain
B. Use an antenna with a higher front-to-back ratio
C. Take precautions to ensure that the antenna cannot be pointed in their direction when they are present
D. All these choices are correct
        """
G0A11 = """
G0A11. What precaution should be taken if you install an indoor transmitting antenna?
A. Locate the antenna close to your operating position to minimize feed-line radiation
B. Position the antenna along the edge of a wall to reduce parasitic radiation
C. Make sure that MPE limits are not exceeded in occupied areas
D. Make sure the antenna is properly shielded
        """
G0A12 = """
G0A12. What stations are subject to the FCC rules on RF exposure?
A. All commercial stations; amateur radio stations are exempt
B. Only stations with antennas lower than one wavelength above the ground
C. Only stations transmitting more than 500 watts PEP
D. All stations with a time-averaged transmission of more than one milliwatt
        """


G0B01 = """
G0B01. Which wire or wires in a four-conductor 240 VAC circuit should be attached to fuses or circuit breakers?
A. Only the hot wires
B. Only the neutral wire
C. Only the ground wire
D. All wires
        """
G0B02 = """
G0B02. According to the National Electrical Code, what is the minimum wire size that may be used safely for wiring with a 20-ampere circuit breaker?
A. AWG number 20
B. AWG number 16
C. AWG number 12
D. AWG number 8
        """
G0B03 = """
G0B03. Which size of fuse or circuit breaker would be appropriate to use with a circuit that uses AWG number 14 wiring?
A. 30 amperes
B. 25 amperes
C. 20 amperes
D. 15 amperes
        """
G0B04 = """
G0B04. Where should the station's lightning protection ground system be located?
A. As close to the station equipment as possible
B. Outside the building
C. Next to the closest power pole
D. Parallel to the water supply line
        """
G0B05 = """
G0B05. Which of the following conditions will cause a ground fault circuit interrupter (GFCI) to disconnect AC power?
A. Current flowing from one or more of the hot wires to the neutral wire
B. Current flowing from one or more of the hot wires directly to ground
C. Overvoltage on the hot wires
D. All these choices are correct
        """
G0B06 = """
G0B06. Which of the following is covered by the National Electrical Code?
A. Acceptable bandwidth limits
B. Acceptable modulation limits
C. Electrical safety of the station
D. RF exposure limits of the human body
        """
G0B07 = """
G0B07. Which of these choices should be observed when climbing a tower using a safety harness?
A. Always hold on to the tower with one hand
B. Confirm that the harness is rated for the weight of the climber and that it is within its allowable service life
C. Ensure that all heavy tools are securely fastened to the harness
D. All these choices are correct
        """
G0B08 = """
G0B08. What should be done before climbing a tower that supports electrically powered devices?
A. Notify the electric company that a person will be working on the tower
B. Make sure all circuits that supply power to the tower are locked out and tagged
C. Unground the base of the tower
D. All these choices are correct
        """
G0B09 = """
G0B09. Which of the following is true of an emergency generator installation?
A. The generator should be operated in a well-ventilated area
B. The generator must be insulated from ground
C. Fuel should be stored near the generator for rapid refueling in case of an emergency
D. All these choices are correct
        """
G0B10 = """
G0B10. Which of the following is a danger from lead-tin solder?
A. Lead can contaminate food if hands are not washed carefully after handling the solder
B. High voltages can cause lead-tin solder to disintegrate suddenly
C. Tin in the solder can “cold flow,” causing shorts in the circuit
D. RF energy can convert the lead into a poisonous gas
        """
G0B11 = """
G0B11. Which of the following is required for lightning protection ground rods?
A. They must be bonded to all buried water and gas lines
B. Bends in ground wires must be made as close as possible to a right angle
C. Lightning grounds must be connected to all ungrounded wiring
D. They must be bonded together with all other grounds
        """
G0B12 = """
G0B12. What is the purpose of a power supply interlock?
A. To prevent unauthorized changes to the circuit that would void the manufacturer’s warranty
B. To shut down the unit if it becomes too hot
C. To ensure that dangerous voltages are removed if the cabinet is opened
D. To shut off the power supply if too much voltage is produced
        """
G0B13 = """
G0B13. Where should lightning arrestors be located?
A. Where the feed lines enter the building
B. On the antenna, opposite the feed point
C. In series with each ground lead
D. At the closest power pole ground electrode
        """

#QUESTION POOLS
G1A = [G1A01, G1A02, G1A03, G1A04, G1A05, G1A06, G1A07, G1A08, G1A09, G1A10, G1A11]
G1B = [G1B01, G1B02, G1B03, G1B04, G1B05, G1B06, G1B07, G1B08, G1B09, G1B10, G1B11]
G1C = [G1C01, G1C02, G1C03, G1C04, G1C05, G1C06, G1C07, G1C08, G1C09, G1C10, G1C11]
G1D = [G1D01, G1D02, G1D03, G1D04, G1D05, G1D06, G1D07, G1D08, G1D09, G1D10, G1D11, G1D12]
G1E = [G1E01, G1E02, G1E03, G1E04, G1E05, G1E06, G1E07, G1E08, G1E09, G1E10, G1E11, G1E12]

G2A = [G2A01, G2A02, G2A03, G2A04, G2A05, G2A06, G2A07, G2A08, G2A09, G2A10, G2A11, G2A12]
G2B = [G2B01, G2B02, G2B03, G2B04, G2B05, G2B06, G2B07, G2B08, G2B09, G2B10, G2B11]
G2C = [G2C01, G2C02, G2C03, G2C04, G2C05, G2C06, G2C07, G2C08, G2C09, G2C10, G2C11]
G2D = [G2D01, G2D02, G2D03, G2D04, G2D05, G2D06, G2D07, G2D08, G2D09, G2D10, G2D11]
G2E = [G2E01, G2E02, G2E03, G2E04, G2E05, G2E06, G2E07, G2E08, G2E09, G2E10, G2E11, G2E12, G2E13, G2E14, G2E15]

G3A = [G3A01, G3A02, G3A03, G3A04, G3A05, G3A06, G3A07, G3A08, G3A09, G3A10, G3A11, G3A12, G3A13, G3A14]
G3B = [G3B01, G3B02, G3B03, G3B04, G3B05, G3B06, G3B07, G3B08, G3B09, G3B10, G3B11, G3B12]
G3C = [G3C01, G3C02, G3C03, G3C04, G3C05, G3C06, G3C07, G3C08, G3C09, G3C10, G3C11]

G4A = [G4A01, G4A02, G4A03, G4A04, G4A05, G4A06, G4A07, G4A08, G4A09, G4A10, G4A11, G4A12, G4A13]
G4B = [G4B01, G4B02, G4B03, G4B04, G4B05, G4B06, G4B07, G4B08, G4B09, G4B10, G4B11, G4B12, G4B13]
G4C = [G4C01, G4C02, G4C03, G4C04, G4C05, G4C06, G4C07, G4C08, G4C09, G4C10, G4C11, G4C12]
G4D = [G4D01, G4D02, G4D03, G4D04, G4D05, G4D06, G4D07, G4D08, G4D09, G4D10, G4D11]
G4E = [G4E01, G4E02, G4E03, G4E04, G4E05, G4E06, G4E07, G4E08, G4E09, G4E10, G4E11]

G5A = [G5A01, G5A02, G5A03, G5A04, G5A05, G5A06, G5A07, G5A08, G5A09, G5A10, G5A11, G5A12]
G5B = [G5B01, G5B02, G5B03, G5B04, G5B05, G5B06, G5B07, G5B08, G5B09, G5B10, G5B11, G5B12, G5B13, G5B14]
G5C = [G5C01, G5C02, G5C03, G5C04, G5C05, G5C06, G5C08, G5C09, G5C10, G5C11, G5C12, G5C13, G5C14]

G6A = [G6A01, G6A02, G6A03, G6A04, G6A05, G6A06, G6A07, G6A08, G6A09, G6A10, G6A11, G6A12]
G6B = [G6B01, G6B02, G6B03, G6B04, G6B05, G6B06, G6B07, G6B08, G6B10, G6B11, G6B12]

G7A = [G7A01, G7A02, G7A03, G7A04, G7A05, G7A06, G7A07, G7A08,]
G7B = [G7B01, G7B02, G7B03, G7B04, G7B05, G7B06, G7B07, G7B08, G7B09, G7B10, G7B11]
G7C = [G7C01, G7C02, G7C03, G7C04, G7C05, G7C06, G7C07, G7C08, G7C09, G7C10, G7C11, G7C12, G7C13, G7C14]

G8A = [G8A01, G8A02, G8A03, G8A04, G8A05, G8A06, G8A07, G8A08, G8A09, G8A10, G8A11, G8A12, G8A13, G8A14]
G8B = [G8B01, G8B02, G8B03, G8B04, G8B05, G8B06, G8B07, G8B08, G8B09, G8B10, G8B11, G8B12, G8B13]
G8C = [G8C01, G8C02, G8C03, G8C04, G8C05, G8C06, G8C06, G8C07, G8C08, G8C09, G8C10, G8C11, G8C12, G8C13, G8C14, G8C15, G8C16]

G9A = [G9A01, G9A02, G9A03, G9A04, G9A05, G9A06, G9A07, G9A08, G9A09, G9A10, G9A11]
G9B = [G9B01, G9B02, G9B03, G9B04, G9B05, G9B06, G9B07, G9B08, G9B09, G9B10, G9B11, G9B12]
G9C = [G9C01, G9C02, G9C03, G9C04, G9C05, G9C07, G9C08, G9C09, G9C10, G9C11,]
G9D = [G9D01, G9D02, G9D03, G9D04, G9D05, G9D06, G9D07, G9D08, G9D09, G9D10, G9D11, G9D12]

G0A = [G0A01, G0A02, G0A03, G0A04, G0A05, G0A06, G0A07, G0A08, G0A09, G0A10, G0A11, G0A12]
G0B = [G0B01, G0B02, G0B03, G0B04, G0B05, G0B06, G0B07, G0B08, G0B09, G0B10, G0B11, G0B12, G0B13]



#ANSWER POOLS
ansG1A = ["c", "b", "b", "d", "a", "c", "d", "b", "c", "d", "b"]
ansG1B = ["c", "a", "a", "c", "b", "d", "b", "b", "d", "c", "a"]
ansG1C = ["a", "c", "a", "a", "c", "d", "c", "d", "c", "c", "d"]
ansG1D = ["a", "c", "c", "a", "a", "a", "c", "b", "c", "b", "d", "c"]
ansG1E = ["a", "d", "a", "d", "c", "c", "d", "b", "a", "a", "d", "a"]

ansG2A = ["a", "b", "a", "a", "c", "d", "b", "b", "d", "b", "c", "b"]
ansG2B = ["c", "b", "c", "b", "c", "a", "c", "a", "a", "b", "c",]
ansG2C = ["d", "a", "c", "d", "b", "d", "a", "c", "c", "d", "d"]
ansG2D = ["a", "d", "b", "b", "c", "c", "d", "d", "c", "b", "a"]
ansG2E = ["d", "b", "d", "d", "b", "b", "b", "d", "c", "d", "c", "d", "b", "d", "c"]

ansG3A = ["a", "b", "c", "d", "d", "d", "d", "d", "a", "c", "d", "b", "c", "b"]
ansG3B = ["d", "d", "a", "a", "a", "c", "a", "b", "c", "b", "a", "d"]
ansG3C = ["a", "a", "c", "d", "c", "b", "d", "a", "b", "b", "d"]

ansG4A = ["b", "c", "c", "b", "c", "c", "a", "d", "c", "b", "b", "c", "a"]
ansG4B = ["d", "d", "a", "d", "d", "c", "b", "a", "d", "a", "c", "b", "c"]
ansG4C = ["b", "c", "c", "a", "d", "c", "a", "a", "d", "a", "c", "d"]
ansG4D = ["a", "b", "d", "c", "d", "a", "c", "c", "b", "a", "b"]
ansG4E = ["c", "d", "a", "b", "c", "c", "d", "a", "b", "b", "d"]

ansG5A = ["c", "b", "d", "c", "d", "a", "d", "c", "b", "d", "b", "d"]
ansG5B = ["b", "c", "b", "a", "a", "b", "c", "d", "b", "c", "b", "b", "b", "b"]
ansG5C = ["c", "a", "a", "d", "b", "a", "a", "d", "c", "c", "c", "b", "c", "d"]

ansG6A = ["c", "b", "b", "c", "c", "b", "a", "d", "b", "a", "c", "a",]
ansG6B = ["c", "b", "a", "c", "d", "d", "a", "d", "a", "b", "c"]

ansG7A = ["b", "c", "a", "a", "b", "d", "a", "c", "c", "d", "b", "c", "a"]
ansG7B = ["b", "d", "b", "a", "c", "a", "d", "b", "c", "b", "b"]
ansG7C = ["b", "d", "b", "d", "d", "a", "a", "d", "b", "b", "d", "c", "d", "a"]

ansG8A = ["b", "b", "d", "b", "d", "d", "a", "d", "a", "c", "a", "d", "c", "b"]
ansG8B = ["b", "b", "a", "d", "c", "d", "b", "b", "d", "b", "c", "a", "c"]
ansG8C = ["c", "a", "c", "c", "a", "b", "b", "b", "b", "c", "d", "a", "d", "c", "c", "d",]

ansG9A = ["a", "b", "d", "c", "b", "d", "d", "b", "a", "d", "a"]
ansG9B = ["b", "b", "d", "a", "c", "c", "b", "a", "a", "d", "c", "a"]
ansG9C = ["a", "b", "a", "b", "a", "c", "d", "b", "d", "a", "a"]
ansG9D = ["a", "d", "c", "a", "d", "a", "a", "b", "a", "b", "d", "a"]

ansG0A = ["a", "d", "d", "d", "a", "a", "a", "c", "b", "c", "c", "d"]
ansG0B = ["a", "c", "d", "b", "b", "c", "b", "b", "a", "a", "d", "c", "a"]




amirunning = True
qpool = 12

#BEGINNING
print( "Welcome to your General Practice Test!\n" )
time.sleep(1.50)
while amirunning == True and qpool == 12:
    print( "Which subelement would you like to study? Enter the corresponding number:\n" )
    time.sleep(1.50)
    print ( "G1 - COMMISSION'S RULES\n" )
    print ( "G2 - OPERATING PROCEDURES\n" )
    print ( "G3 - RADIO WAVE PROPAGATION\n" )
    print ( "G4 - AMATEUR RADIO PRACTICES\n" )
    print ( "G5 - ELECTRICAL PRINCIPLES\n" )
    print ( "G6 - CIRCUIT COMPONENTS\n" )
    print ( "G7 - PRACTICAL CIRCUITS\n" )
    print ( "G8 - SIGNALS AND EMISSIONS\n" )
    print ( "G9 - ANTENNAS AND FEED LINES\n" )
    print ( "G0 - ELECTRICAL AND RF SAFETY\n" )
    print ( "Full practice test (enter 10)\n" )
    print ( "Exit (enter 11)\n")
    test = input("   ")
    if test == "1":
        qpool = 1
    if test == "2":
        qpool = 2
    if test == "3":
        qpool = 3
    if test == "4":
        qpool = 4
    if test == "5":
        qpool = 5
    if test == "6":
        qpool = 6
    if test == "7":
        qpool = 7
    if test == "8":
        qpool = 8
    if test == "9":
        qpool = 9
    if test == "0":
        qpool = 0
    if test == "10":
        qpool = 10
    if test == "11":
        amirunning = False


#TESTS
    if qpool == 1:
        clearScreen()
        while qpool == 1:
            questNum = 5
            correct = 0
            Q1 = questionPick(G1A, ansG1A)
            if Q1 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q2 = questionPick(G1B, ansG1B)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q3 = questionPick(G1C, ansG1C)
            if Q3 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q4 = questionPick(G1D, ansG1D)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q5 = questionPick(G1E, ansG1E)
            if Q5 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            goodAnswer(correct, questNum)
            clearScreen()
            redo = input( "Would you like to continue practicing this section? Enter 1 for yes, or 0 for no:   ")
            if int(redo) == 1:
                clearScreen()
            else:
                clearScreen()
                qpool = 12

            if qpool != 1:
                break
        
    if qpool == 2:
        clearScreen()
        while qpool == 2:
            questNum = 5
            correct = 0
            Q1 = questionPick(G2A, ansG2A)
            if Q1 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q2 = questionPick(G2B, ansG2B)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q3 = questionPick(G2C, ansG2C)
            if Q3 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q4 = questionPick(G2D, ansG2D)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q5 = questionPick(G2E, ansG2E)
            if Q5 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            goodAnswer(correct, questNum)
            clearScreen()
            redo = input( "Would you like to continue practicing this section? Enter 1 for yes, or 0 for no:   ")
            if int(redo) == 1:
                clearScreen()
            else:
                clearScreen()
                qpool = 12
            if qpool != 2:
                break  

    if qpool == 3:
        clearScreen()
        while qpool == 3:
            questNum = 3
            correct = 0
            Q1 = questionPick(G3A, ansG3A)
            if Q1 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q2 = questionPick(G3B, ansG3B)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q3 = questionPick(G3C, ansG3C)
            if Q3 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            goodAnswer(correct, questNum)
            clearScreen()
            redo = input( "Would you like to continue practicing this section? Enter 1 for yes, or 0 for no:   ")
            if int(redo) == 1:
                clearScreen()
            else:
                clearScreen()
                qpool = 12
            if qpool != 3:
                break

    if qpool == 4:
        clearScreen()
        while qpool == 4:
            questNum = 5
            correct = 0
            Q1 = questionPick(G4A, ansG4A)
            if Q1 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q2 = questionPick(G4B, ansG4B)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q3 = questionPick(G4C, ansG4C)
            if Q3 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q4 = questionPick(G4D, ansG4D)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q5 = questionPick(G4E, ansG4E)
            if Q5 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            goodAnswer(correct, questNum)
            clearScreen()
            redo = input( "Would you like to continue practicing this section? Enter 1 for yes, or 0 for no:   ")
            if int(redo) == 1:
                clearScreen()
            else:
                clearScreen()
                qpool = 12
            if qpool != 4:
                break

    if qpool == 5:
        clearScreen()
        while qpool == 5:
            questNum = 3
            Q1 = questionPick(G5A, ansG5A)
            if Q1 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q2 = questionPick(G5B, ansG5B)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q3 = questionPick(G5C, ansG5C)
            if Q3 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            goodAnswer(correct, questNum)
            clearScreen()
            redo = input( "Would you like to continue practicing this section? Enter 1 for yes, or 0 for no:   ")
            if int(redo) == 1:
                clearScreen()
            else:
                clearScreen()
                qpool = 12
            correct = 0
            if qpool != 5:
                break

    if qpool == 6:
        clearScreen()
        while qpool == 6:
            questNum = 2
            correct = 0
            Q1 = questionPick(G6A, ansG6A)
            if Q1 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q2 = questionPick(G6B, ansG6B)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            goodAnswer(correct, questNum)
            clearScreen()
            redo = input( "Would you like to continue practicing this section? Enter 1 for yes, or 0 for no:   ")
            if int(redo) == 1:
                clearScreen()
            else:
                clearScreen()
                qpool = 12
            if qpool != 6:
                break
    
    if qpool == 7:
        clearScreen()
        while qpool == 7:
            questNum = 3
            Q1 = questionPick(G7A, ansG7A)
            if Q1 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q2 = questionPick(G7B, ansG7B)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q3 = questionPick(G7C, ansG7C)
            if Q3 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            goodAnswer(correct, questNum)
            clearScreen()
            redo = input( "Would you like to continue practicing this section? Enter 1 for yes, or 0 for no:   ")
            if int(redo) == 1:
                clearScreen()
            else:
                clearScreen()
                qpool = 12
            correct = 0
            if qpool != 7:
                break
    
    if qpool == 8:
        clearScreen()
        while qpool == 8:
            questNum = 3
            correct = 0
            Q1 = questionPick(G8A, ansG8A)
            if Q1 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q2 = questionPick(G8B, ansG8B)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q3 = questionPick(G8C, ansG8C)
            if Q3 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            goodAnswer(correct, questNum)
            clearScreen()
            redo = input( "Would you like to continue practicing this section? Enter 1 for yes, or 0 for no:   ")
            if int(redo) == 1:
                clearScreen()
            else:
                clearScreen()
                qpool = 12
            if qpool != 8:
                break
    
    if qpool == 9:
        clearScreen()
        while qpool == 9:
            questNum = 4
            correct = 0
            Q1 = questionPick(G9A, ansG9A)
            if Q1 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q2 = questionPick(G9B, ansG9B)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q3 = questionPick(G9C, ansG9C)
            if Q3 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q4 = questionPick(G9D, ansG9D)
            if Q4 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            goodAnswer(correct, questNum)
            clearScreen()
            redo = input( "Would you like to continue practicing this section? Enter 1 for yes, or 0 for no:   ")
            if int(redo) == 1:
                clearScreen()
            else:
                clearScreen()
                qpool = 12
            if qpool != 9:
                break
    
    if qpool == 0:
        clearScreen()
        while qpool == 0:
            questNum = 2
            correct = 0
            Q1 = questionPick(G0A, ansG0A)
            if Q1 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q2 = questionPick(G0B, ansG0B)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            goodAnswer(correct, questNum)
            clearScreen()
            redo = input( "Would you like to continue practicing this section? Enter 1 for yes, or 0 for no:   ")
            if int(redo) == 1:
                clearScreen()
            else:
                clearScreen()
                qpool = 12
            if qpool != 0:
                break

    if qpool == 10:
        clearScreen()
        while qpool == 10:
            questNum = 35
            correct = 0

            Q1 = questionPick(G1A, ansG1A)
            if Q1 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q2 = questionPick(G1B, ansG1B)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q3 = questionPick(G1C, ansG1C)
            if Q3 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q4 = questionPick(G1D, ansG1D)
            if Q2 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q5 = questionPick(G1E, ansG1E)
            if Q5 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q6 = questionPick(G2A, ansG2A)
            if Q6 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q7 = questionPick(G2B, ansG2B)
            if Q7 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q8 = questionPick(G2C, ansG2C)
            if Q8 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q9 = questionPick(G2D, ansG2D)
            if Q9 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q10 = questionPick(G2E, ansG2E)
            if Q10 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q11 = questionPick(G3A, ansG3A)
            if Q11 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q12 = questionPick(G3B, ansG3B)
            if Q12 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q13 = questionPick(G3C, ansG3C)
            if Q13 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q14 = questionPick(G4A, ansG4A)
            if Q14 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q15 = questionPick(G4B, ansG4B)
            if Q15 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q16 = questionPick(G4C, ansG4C)
            if Q16 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q17 = questionPick(G4D, ansG4D)
            if Q17 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q18 = questionPick(G4E, ansG4E)
            if Q18 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q19 = questionPick(G5A, ansG5A)
            if Q19 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q20 = questionPick(G5B, ansG5B)
            if Q20 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q21 = questionPick(G5C, ansG5C)
            if Q21 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q22 = questionPick(G6A, ansG6A)
            if Q22 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q23 = questionPick(G6B, ansG6B)
            if Q23 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q24 = questionPick(G7A, ansG7A)
            if Q24 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q25 = questionPick(G7B, ansG7B)
            if Q25 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q26 = questionPick(G7C, ansG7C)
            if Q26 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q27 = questionPick(G8A, ansG8A)
            if Q27 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q28 = questionPick(G8B, ansG8B)
            if Q28 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q29 = questionPick(G8C, ansG8C)
            if Q29 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q30 = questionPick(G9A, ansG9A)
            if Q30 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q31 = questionPick(G9B, ansG9B)
            if Q31 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q32 = questionPick(G9C, ansG9C)
            if Q32 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q33 = questionPick(G9D, ansG9D)
            if Q33 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q34 = questionPick(G0A, ansG0A)
            if Q34 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            Q35 = questionPick(G0B, ansG0B)
            if Q35 == True:
                correct += 1
                print("Correct!")
            else:
                print("Sorry! Incorrect.")
            time.sleep(1.50)
            clearScreen()

            goodAnswer(correct, questNum)
            clearScreen()
            redo = input( "Would you like to continue practicing this section? Enter 1 for yes, or 0 for no:   ")
            if int(redo) == 1:
                clearScreen()
            else:
                clearScreen()
                qpool = 12
            if qpool != 10:
                break

    if amirunning != True:
        print( "See you later!")
        sys.exit()
