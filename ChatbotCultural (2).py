#imports 
from random import *
from time import *
from datetime import *
from sys import *
from gtts import gTTS
from playsound import playsound
#infomation/data
Regions = ['a. Northern', 'b. Southern', 'c. Western', 'd. Eastern', 'e. North Eastern']#regions of india

End_salutations=['\n Bye, I have to help another user', '\n Bye, see you soon'] 
#festivals dictionaries
N_festivals={'\n Holi ': 'is a lively festival that is celebrated in most parts of India, but it is a celebration done with utmost magnificence in various forms particularly in North India. The festival is famous enough for the entire world to relate playing with colours to India, since that is what Holi celebration is mostly about. Lath mar Holi is a very famous celebration that takes place in the small town of Barsana in Uttar Pradesh. Playing with water and colours, forming human pyramids and breaking a pot of butter tied on the top are some of the many events that take place during Holi. It falls in the month of March every year.', 
'\n Baisakhi': 'Mainly celebrated by Sikhs, Baisakhi or Vaisakhi is a festival that takes place during the month of April every year. It commemorates the formation of Khalsa, the time of harvest and acts as the mark of the New Year for the followers of Sikhism.Bhangra, the popular Punjabi folk dance sees its origin from Baisakhi. It was a dance form that began to celebrate the harvest festival; therefore, celebrations compulsorily include Bhangra performance.',
'\n Lohri': 'Celebrated by both Hindus and Sikhs, Lohri is a winter festival celebrated mainly in Punjab. It usually falls on 14th January, which marks the end of the winter season.The festival is celebrated by making a bonfire and having classic traditional food of Punjab like sarson ka saag(a vegetable of spinach), makki di roti(indian flat bread made with chickpea flour) and food made out of jaggery, groundnuts, etc.The celebrations are accompanied by Bhangra, folk songs exclusively sung during Lohri, etc.',
'\n Diwali' : ' or Deepavali is the most spectacular festival celebrated in the Indian subcontinent. Autumn heralds in this Hindu festival of lights that is celebrated across the length and breadth of the country. The celebrations are marked by people decorating their homes with candles, earthen lamps, and lights, bursting crackers, and exchanging gifts and sweets with friends and family. Since it is celebrated on a new moon night, these sparkling lamps and lights add a magical feel to the whole scenario. A festival that commemorates Lord Rama’s return with his wife after 14 years of exile and his triumph over Ravana, Diwali symbolizes the ultimate victory of good over evil.'
}
S_festivals={'\n Onam' : 'is a Hindu festival that originated in Kerala. It is celebrated as a rice harvest festival, to honour the Vamana avatar of Lord Vishnu and homecoming of Emperor Mahabali. This is a grand festival for Malayali Hindus and it falls during the months of August or September every year.Many events that take place as part of Onam celebrations include performances of pulikali (tiger dance), onathallu (martial arts), onavillu (music), or making beautiful flower arrangements called pookkalam. Boat races or Vallam Kali also take place during this time.',
'\n Natyanjali Dance Festival': 'Blending spirituality with art and dance, the Natyanjali Dance Festival is celebrated as a dedication to Lord Nataraja, a depiction of Lord Shiva. This is a 5-day-long festival that is celebrated during the months of February or March, during Maha Shivarathri.The festival takes place in Chidambaram, Tamil Nadu, which is located around 230 km from Chennai. Performers from all over the country who take part in this festival hold the event in the highest regard and put up the best dance performances every year.',
'\n Pongal ': 'is a harvest festival celebrated in Tamil Nadu, during 14th or 15th January. It is celebrated as Makara Sankranti in the rest of the country while it is called Pongal in Tamil Nadu. This important Hindu festival is celebrated for 4 days, with each day having a different purpose.Crops, like sugarcane, turmeric and cereals, are harvested during this season, and the festival is celebrated as a way of thanking the nature for giving us the grains.'}
E_festivals={'\n Durga Puja' : 'is a symbol of cultural identity for the Bengalis. It is celebrated with much fanfare and gaiety for four days. One of the major festivals of India, it is particularly popular in West Bengal, Assam, Odisha, Tripura, Jharkhand, and Bihar. During Durga Puja, huge clay idols of the ten-armed Goddess Durga and her four children are worshipped in specially made mandaps. People dress up in new clothes and go pandal-hopping with family and friends. The festival culminates with the immersion of the idol of the goddess in water.'
,'\n Chhath Puja': ' is an ancient Hindu festival observed over four days to show reverence to the Sun God and his wife, and seek their blessings for happiness and good health. Fasting, abstaining from drinking water, bathing in rivers, and offering prayers to the sun during sunrise and sunset are integral parts of it. The festival is observed by families, generation after generation, without a break. As per tradition, one can take a break from the observance only if there is a death in the family.'
,'\nHornbill Festival' : 'also Called the ‘Festival of Festivals’, offers a fine showcase of the traditions and cultures of Nagaland. The weeklong festival is celebrated at the Naga Heritage Village, which is around 11 km from the capital city of Kohima. During the festival, you can see colorful performances by the participants, traditional food fairs, art and crafts of the land, games, parades, and religious ceremonies that uphold the beauty of Nagaland in a unique manner. All tribes of the state participate in these celebrations, making it a true extravaganza.'}

NE_festivals={'\n Majuli Festival(Assam)': 'People who have been a part of Majuli festival often describe it as one of the most pleasing and beautiful festivals of Northeast India. Celebrated at Garamur, on the banks of the river Luit, the Majuli Festival is a four day long festival which highlights the exclusive Neo-Vaishnavite culture of the Majuli region in particular, and of Assam as a whole.During the festival, a grand exhibition is organised, where traditional items, such as pottery, tribal garment and handicrafts, valuable items made of bamboo and cane are displayed for sale.',
'\n Nongkrem Dance Festival(Meghalaya)':'The Nongkrem Dance is celebrated to appease the almighty Goddess, ‘Ka Blei Synshar’, in the hope of receiving a rich harvest and prosperity of the people. \n Nongkrem Dance Festival, a five day harvest festival celebrated by the Khasi tribe, is the most important festival of the Khyrim state and a significant event in the festivals of Northeast India. Nongkrem Dance is a religious dance celebration in Meghalaya, and is fundamentally celebrated with colossal enthusiasm and intensity by the Khasi tribe. In Khasi Hills, the Nongkrem Dance Carnival is called Shad Nongkrem and is celebrated each year at Smit, which is the capital of Khyrem Syiemship, close to Shillong. ',
'\n Losar Festival(Arunachal Pradesh)':'One of the most significant festivals of the Buddhist Community in Tawang, Losar commemorates the advent of the new year. The word Losar is derived from two Tibetan words, ‘lo’ which means ‘year’ and ‘sar’ which means ‘new’. The festival is observed to ward off evil spirits and celebrate the arrival of the New Year. \n In this fifteen day long festival, the first three days are very important. On the first day of Losar, people clean up their homes and decorate it with 8 auspicious symbols – the precious umbrella, 2 golden fish, a victory banner, a right coiled white conch shell, a lotus flower, the Dharma Wheel, a vase of treasure, and the Eternal Knot, collectively called Tashi Dargy. \nThe following day is reserved for the King and is called Gyalpo Losar. While the day is spent visiting friends and family and indulging in the traditonal masked dance –Monpa dance– at night, people burn firecrackers to get rid of evil spirits. \n The third day of Losar is spent visiting the local monastery and offering prayers, raising flags, donating food and clothes and exchanging gifts.',
'\n Aoling festival(Nagaland)':'The arrival of spring in the first week of April is celebrated with the Aoling festival by the Konyak Nagas.\n Another festival in the many unique festivals of Northeast India, the Aoling festival continues for six days and the first day of the festival is recognised as the Konyak New Year. During the festival, the members of the tribe perform rituals such as animal sacrifices, dances, feasts and cleanliness drives around the village.',
'\n Kharchi Puja(Tripura)':'One of most renowned pujas in Tripura, Kharchi Puja is a sacred procedure of offering reverence to the Mother Earth. The Kharchi Puja continues for seven days and the people of Tripura with utmost dedication offer worship to the Fourteen Deities who are worshipped during Kharchi Puja.',
'\n Cheiraoba Festival(Manipur)':'Cheiraoba, also called Sajibu Cheiraoba, is the celebration of New Year in Manipur.\n During the festival, special festive dishes are prepared to be offered to the deities. Climbing the Cheiraoching peak is also a part of the festival as climbing signifies elevation to greater heights in their worldly life.'
}


# heritage site dictionaries
N_hs={'\n The Taj Mahal':' is an immense mausoleum of white marble in Agra, is one of the universally admired buildings of world heritage. Taj Mahal is one of the new seven wonders of the world.\n Cities of Fatehpur Sikri and Delhi also carry some great exhibits from the Mughal architecture. ', 
'\n The Golden Temple ':' The Golden Temple, also known as Harmandir Sahib, meaning "abode of God"  is a Gurdwara located in the city of Amritsar, Punjab, India. It is the preeminent spiritual site of Sikh religion.\n The Golden Temple is an open house of worship for all men and women, from all walks of life and faith. It has a square plan with four entrances, has a circumambulation path around the pool. The complex is a collection of buildings around the sanctum and the pool. One of these is Akal Takht, the chief center of religious authority of Sikhism.Additional buildings include a clock tower, the offices of Gurdwara Committee, a Museum and a langar – a free Sikh community run kitchen that serves a simple vegetarian meal to all visitors without discrimination. Over 100,000 people visit the holy shrine daily for worship. The Gurdwara complex has been nominated as a UNESCO World Heritage Site .',
'\n Varanasi': 'a city on the banks of the River Ganga, is considered one of the oldest continuously inhabited cities in the world .',
'\n Khajuraho temples':'Khajuraho temples constitute another famous world heritage site.',
'\n The Mahabodhi Temple ':'The Mahabodhi Temple complex at Bodh Gaya, in Bihar state was built by Emperor Ashoka in 260 BC. This temple  marks the enlightenment of Siddhartha Gautam Buddha'}
S_hs={'\n Temples of Mahabalipuram' :'Constructed In Approximately around 7th and 8th centuries but till today their architectural brilliance and beauty is unsurpassable .Its unique concept and construction. You can notice this everywhere, whether you visit the rock-carved monuments of Mahabalipuram which form the largest open – air bas relief in the world or the numerous temples which till date attract thousands of tourists throughout the year.The architectural brilliance of the temples of the place is such that they found itself a place in the esteemed list of world heritage sites back in the year 1984.',
'\n Western Ghats': ' Western Ghats which span over a huge area of 60, 000 square kilometre. The presence of tea, coffee and various spices plantations add on the colour green considerably to an already gorgeous place, so much that it is referred as one of the eight hottest hotspots of biological diversity in the whole world. TheWestern Ghats spread over Karnataka, Kerala and Tamil Nadu covering many amazing places like Ooty, Coonoor, Munnar, Kodaikanal, Bandipur and many more in between.',
'\n Monuments of Hampi': ' Once the capital of the rich and powerful Vijayanagar empire, today Hampi stands proudly as a sight of architectural wonders and an important religious centre.The architecture and construction of the place will leave you wondering how it was possible at a time with no modern machinery, tools or technology.It is famous for its numerous temples and markets which though today are in ruins but will still leave you speechless. One important Hindu temple that you must visit if there is Virupaksha Temple.',
'\n The Famous Chola Temples': 'Cholas were known widely for their arts and crafts brilliance which is clearly reflected in their construction of numerous temples. Visiting these temples in Tamil Nadu will surely be a treat for the eyes!  The powerful Chola Dynasty which is also known as the dynasty to rule the Southern India for the longest duration is till today a matter of pride for the Tamilians.  These gorgeous temples are a symbol of pride for the Tamilians since 11th and 12th centuries. Though the place is a house to many temples but three most famous temples which till today are the most visited cultural heritage sites are- the Brihadeeswara temple at Thanjavur and at Gangaikonda Cholapuram and the Airavateswara temple at Darasuram.', 
'\n Mysore ': 'Mysore is the most preferred place to go for all the history lovers due to its rich and glorious heritage which is very much evident in its numerous temples, palaces and monuments.Once an erstwhile capital of the famous Wadiyar dynasty, today this place is filled with many heritage sites which hold great historic significance. Whether you visit the ancient Chamundi Temple or the gorgeous Somnathpura Temple or the wonderful Chennakesava Temple, you are sure to witness some exceptional beauty. Mysore Palace is also one beautiful and grand place to visit. Another name that rings in the mind at the mention of Mysore, is that of Tipu Sultan who is lovingly known as the Tiger of Mysore. You can find his legacy spread all over the place.' }
E_hs={'\n Sun Temple':' Bhubaneswar is considered to be the "City of Temples". Sun temple is present in small town of Konark ',
'\n Bihar Sharif': 'Bihar Sharif is an important pilgrimage centre for Muslims all over Bihar.',
'\n In Bihar Village Harinagar':' Bajrang Bali temple is very famous for Hindu people.',
'\n Dakshineswar Kali Temple' :' is a famous historical Kali temple in West Bengal. ',
'\n Kalighat Kali Temple':'Kalighat Kali Temple  in Kolkata is the most important of all Shakti Peethas in India.',
 '\n Belur Math ': 'in Kolkata is the headquarters of the Ramkrishna Mission founded by Swami Vivekananda.',
 '\n Bodh Gaya ': 'Bodh Gaya is the city sacred to Buddhism. There are also other cities sacred to Jains in Bihar and Jharkhand.',
}
W_hs={'Jaipur': 'Jaipur is a vibrant amalgamation of the old and the new. The capital of the royal state of Rajasthan, Jaipur has been ruled by Rajput kingdoms for many centuries and developed as a planned city in the 17th century AD. Along with Delhi and Agra, Jaipur forms the Golden Triangle, one of the most famous tourist circuits of the country.', 
'The Open gallery of Rajasthan, Shekhawati, Rajasthan':'Shekhawati is a semi-arid getaway full of open air galleries, enchanting havelis & palaces and legendary forts. This region has been recognised as the open art gallery of Rajasthan"" having the largest concentration of frescos in the world.',
'Udaipur ':'Udaipur, also known as the City of Lakes, is the crown jewel of the state of Rajasthan. It is surrounded by the beautiful Aravalli Hills in all directions, making this city as lovely as it is. This \'Venice of the East\' has an abundance of natural beauty, mesmerising temples and breathtaking architecture which makes it a must-visit destination in India. A boat ride through the serene waters of Lake Pichola will be enough to prove to you why Udaipur is the pride of Rajasthan.',
'Jodhpur, The Blue City ':'Also Known as the "Gateway to Thar", it is famous for its Mehrangarh fort, blue houses, temples, sweets and snacks. Apart from the fort, there are multiple temples, lakes, shopping streets that are like a mirage from a bygone era.',
'Ajanta and Ellora caves, Maharashtra, The World Heritage Caves' :'Ajanta and Ellora caves are considered to be one of the most important tourist destinations in the world owing to the magnificent paintings of Ajanta and well-carved sculptures of Ellora. The rock-cut caves containing carvings are the finest example of Indian paintings and sculpture.',
'Patan,Gujrat ': 'Rani Ka Vav, the latest Indian entrant to the list of UNESCO World Heritage Site is situated here, making Patan one of the newest tourist hubs in India.'}


#geographic dictionaries
N_G ={'\n North India':' is a loosely defined region consisting of the northern part of India. The dominant geographical features of North India are the Indus-Gangetic Plain and the Himalayas, which demarcate the region from the Tibetan Plateau and Central Asia.',
'\n Culture':'North India has been the historical centre of the Mughal Empire and the British Indian Empire. It has a diverse culture, and includes the Hindu pilgrimage centres of Char Dham, Haridwar, Varanasi, Ayodhya, Mathura, Allahabad, Vaishno Devi and Pushkar, the Buddhist pilgrimage centres of Sarnath and Kushinagar, the Sikh Golden Temple as well as world heritage sites such as the Nanda Devi Biosphere Reserve, Khajuraho temples, Hill Forts of Rajasthan, Jantar Mantar (Jaipur), Bhimbetka Caves, Sanchi monuments, Qutb Minar, Red Fort, Agra Fort, Fatehpur Sikri and the Taj Mahal.'
, '\n States ' : 'The term North Indian Culture officially describes the cultural heritage of the seven North Indian states of Punjab, Jammu & Kashmir, Chandigarh (Union Territory), Haryana, Delhi, Himachal Pradesh, and Uttar Pradesh (which itself means "Northern State").\n North Indian culture reflects the diversity of traditions and customs of the vast region it encompasses. North Indian Culture is mainly in Indo-Aryan traditions and customs, with the assimilation of — and impact from — other cultures over long periods of history. North Indian culture reflects the diversity of traditions and customs of the vast region it encompasses.'}
S_G={'\n South India ':'South India is bounded by the Bay of Bengal in the east, the Arabian Sea in the west and the Indian Ocean in the south. ',
     '\n States':'South India is the area including the Indian states of Andhra Pradesh, Karnataka, Kerala, Tamil Nadu and Telangana as well as the union territories of Andaman and Nicobar, Lakshadweep and Puducherry, occupying 19.31% of India\'s area.',
     '\n Geographical features':'The geography of the region is diverse with two mountain ranges - the Western and Eastern Ghats, bordering the plateau heartland. Godavari, Krishna, Kaveri, Tungabhadra and Vaigai rivers are important non-perennial sources of water.'}
W_G ={'\n Western India': ' is a loosely defined region of India consisting of its western part. The Ministry of Home Affairs in its Western Zonal Council Administrative division includes the states of Goa, Gujarat, and Maharashtra along with the Union territory of Dadra and Nagar Haveli and Daman and Diu,  while the Ministry of Culture and some historians also include the state of Rajasthan. The Geological Survey of India includes Maharashtra but excludes Rajasthan whereas Ministry of Minority Affairs includes Karnataka but excludes Rajasthan.',
'\n Culture of Maharashtra': 'Maharashtrian culture derives from the ancient Hindu Vedic culture influenced deeply by the Maratha Empire. Maharashtrians take great pride in the Maratha Empire, and many places in Maharashtra are named after the founder of the Empire, Shivaji. Marathi literature and cinema are popular in the state as well as across India. Bollywood has had a huge impact on the lifestyle and culture of this part of India as the industry is primarily located in Mumbai.',
'\n Culture of Gujarat ':'Gujarati culture is a blend of Indian culture and foreign influence. It has been influenced by the Parsis, who migrated to Gujarat from Persia about a 1000 years ago. Gujarat also saw Turkic and Mughal conquests, as well as a constant stream of back and forth migrations to and from Sindh and Rajasthan, which helped shape the unique cultural landscape of the state. Cultural Events like Rann Utsav, International Kite Festival and Global Garba festivals have been started in Gujarat to showcase its culture internationally.',
'\n Culture of Goa ':'Goa\'s culture is a unique blend of Indian and Portuguese cultures, as a result of it formerly being part of Portuguese India for 450 years. The state is popular amongst tourists for its beaches, Goan cuisine, temples, churches and architecture. The Churches and Convents of Goa have been declared as a World Heritage Site by UNESCO.', 
'\n States ':'Dadra and Nagar Haveli and Daman and Diu, Goa ,Gujarat, Karnataka, Maharashtra, Rajasthan' }

NE_G ={'\n Northeast India':'is the easternmost region of India representing both a geographic and political administrative division of the country. It comprises eight states – Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim and Tripura. ',
'Borders ':'It comprises eight states – Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim and Tripura. The region shares an international border of 5,182 kilometres (3,220 mi) (about 99 percent of its total geographical boundary) with several neighbouring countries – 1,395 kilometres (867 mi) with Tibet Autonomous Region, China in the north, 1,640 kilometres (1,020 mi) with Myanmar in the east, 1,596 kilometres (992 mi) with Bangladesh in the south-west, 97 kilometres (60 mi) with Nepal in the west, and 455 kilometres (283 mi) with Bhutan in the north-west.',
'area': 'It comprises an area of 262,230 square kilometres (101,250 sq mi), almost 8 percent of that of India, and is one of the largest salients (panhandles) in the world.'}

#dictionaries of each region
North = {'a. Geography':N_G,
'b. Languages':'\n The languages that have official status in one or more of the states and union territories located in North India are Hindi, Urdu, Punjabi and English.',
'c. Religions':'\n The religions followed in this region are- Hinduism, Islam, Sikhism, Jainism, Judaism, Christianity, and Buddhism',
'd. Clothes':'\n Women traditionally wear salwar kameez, ghagra choli, sari and phiran. Dupatta is worn to complete the outfit.\n Men traditionally wear kurta, achkan, kameez and sherwani for upper garment, lower garment includes dhoti, churidar, shalwar and Lungi. \n Pagri is usually worn around the head to complete the outfit, especially in rural areas.\n In the states of Punjab, Jammu and Kashmir, Himachal Pradesh and Haryana and Gujarat, traditional dress is Kameez Shalwar.\n In the states of Rajasthan, Uttar Pradesh, Bihar and southern Haryana and Gujarat, it is ghagra choli. \n Pagri is worn in various region styles and is the symbol which shows one\'s status and the respect in which one is held. In urban centres and as well as rural areas western influence can easily be seen nowadays.\nEach state of North India has its own regional forms of clothing:\n1. Uttar Pradesh: Chikan Suit, Pathani Salwar, Kurta Paijama, Sari .\n2. Jammu: Kurta/Dogri suthan and kurta/churidar pajama and kurta.\n3. Kashmir: Phiran and poots.\n4. Himachal Pradesh: Shalwar kameez, Kurta, Churidar, Dhoti, Himachali cap and angarkha.\n5. Punjab/Haryana: Salwar (Punjabi) Suit, Patiala salwar, Punjabi Tamba and Kurta, Sikh Dastar, Phulkari, Punjabi Ghagra\n6. Uttarakhand: Rangwali Phichora\n',
'e. Food':'\n Wheat forms the staple diet of North India and is usually served in the form of roti or chapatis along with subzi (vegetarian curry dishes). A vegetarian diet is a norm almost everywhere except in Kashmir, however, the non-vegetarian food is also popular. Mughlai cuisine, especially that of Lucknow and Delhi, is known for non-vegetarian dishes with a distinctive aroma, taste and with a different style of cooking. Punjabi food is known for being spicy and tasty.\n Some of the popular dishes from- \n Punjab State includes sarson da saag, Makki ki Roti, dal makhani, choley (chickpeas, served with naan or kulcha), choley Bhature (fluffy deep-fried leavened bread ), kadhi pakora, lassi, etc. Punjabi dhabas can be found all over the region. \nRajasthani cuisine is famous for its dishes like daal-baati, churma, etc. A variety of desserts can be found in North India, like Jalebi crispy sugary circular dessert also comes in another variant called imarti, halwa (sweet pudding), gujia], kheer, petha (specially Agra petha), bal mithai (from Kumaon), to name but a few.',
'f. Festivals':N_festivals,
'g. Heritage sites':N_hs,
'h. Literature':'\n North India was the birthplace of Kalidasa, who wrote classic Sanskrit plays like Malavikagnimitram, Abhijnanusakuntalam and Vikramorvasiyam and poems like Raghuvaṃsa, Kumarasambhava, Ṛtusaṃhara and Meghaduta in which the use of imagination and similes remains unequaled by any other literary work.\n Apart from these Sanskrit dramas, Paṇini\'s Ashtadhyayi standardized Sanskrit grammar and phonetics and left an indelible mark on these aspects of Sanskrit. Panini was a grammarian from approximately 5th century BC, his Ashtadhyayi is looked upon as a masterpiece and as a study in brevity and completeness.\n Medieval North India had great literary scholars like Tulsidas, Surdas, Chand Bardai, Amir Khusro whose works Ramcharitmanas, Sur Sagar, Prithiviraj Raso and Khamsa-e-Nizami respectively contributed to the richness of literature.\n Other important writers of this period are Munshi Premchand, Mahavir Prasad Dwivedi, Maithili Sharan Gupt, R N Tripathi and Gopala Sharan Sinha. Premchand\'s works, such as Godaan and Gaban have been translated into various languages, and are known for their subtlety and depiction of human psychology and emotions',
'i. Music':'\n Hindustani classical music or Shastriya Sangeet is the classical music of North India. It is a tradition that originated in Vedic ritual chants and has been evolving since the 12th century. Around the 12th century, Hindustani classical music diverged from what eventually came to be identified as Carnatic classical music. \nIndian classical music has seven basic notes, Sa Re Ga Ma Pa Dha Ni, with five interspersed half-notes, resulting in a 12-note scale. The rhythmic organization is based on rhythmic patterns called Taal. The melodic foundations are called ragas. Noted representatives of Shastriya Sangeet with a worldwide acclaim are Pandit Ravi Shankar and Ustad Ali Akbar Khan.\nThe rich cultural diversity of North India is most clearly shown by the many different folk dance styles found here.\n Starting with Bhangra (men’s dance) and Giddha (women’s dance) from Punjab to Kathak in Uttar Pradesh; from Ghoomar and Kalbeliya dance from Rajasthan to Nati from Himachal Pradesh; \n Karma from Jharkhand to Panthi from Chhattisgarh;\n from Jagars and Pandva Nritya from Uttarakhand to Rouf of Kashmir celebrates the richness of culture and traditions of North India. Kud dance of Jammu & Kashmir is the way to thank local deities in the night of rainy season with the beats of drum like instrument Narsingha. Kathak is one of the eight classical dance forms as conferred by Sangeet Natak Akademi. This dance form traces its origins to the nomadic bards of ancient northern India, known as Kathaks, or storytellers. Some believe it evolved from Lord Krishna\'s raas lilas, forms of which have also evolved into the popular Garba-style dances popular in other parts of region and Gujarat.Raas lilas portrays the love stories of lord Krishna. A dance form which depicts the eternal love. It was quintessential theatre, using instrumental and vocal music along with stylized gestures, to enliven the stories.\n Dance of North India has diverse folk and classical forms. Among the well-known folk dances are \n the bhangra of the Punjab State,\n Ghoomar of Rajasthan state, \n Nati of Himachal Pradesh and \n rouf and bhand pather of Kashmir.',
'j. Dance': '\n Rouf Dance, Jammu & Kashmir – The Rouf is Kashmir’s springtime dance. While performing the Rouf, the performers split themselves in two groups and stand in their respective rows, while facing one another.\n During the dance, the performers bond with their fellow dancers by placing their arms around their shoulders on both sides. Next, the two rows of dancers move in the backward as well as forward direction.\n Dumhal Dance, Kashmir – The Dumhal is a well-known dance form which is performed in Kashmir, primarily by the men of the Wattal tribe. Musical instruments such as the drum add music to the dance. \n Bhangra Dance, Punjab – The Bhangra is a vivacious, robust and extremely popular dance of Punjab which is performed during the festival of Baisakhi. \n This dance form is quite vigorous in nature and is performed primarily by men. The beats of the drums and the dholak add vibrancy to this dance. While doing the Bhangra, a signature step is to raise the leg and raise both hands up in the air. \n Gidda Dance, Punjab – Just as the Bhangra is Punjab’s most important male dance, the Gidda is performed by female dancers. It is a graceful and energetic dance, a form of ring dancing. During the course of the dance, the women break into semi-circles and the dance is accompanied by “boliyan” or folk couplets. \n Raas, Himachal Pradesh – In the Kulu district of HP, the raas is quite popular. It depicts love stories of human beings and is performed during the festival of Dussehra. Raas is also a dance of Gujrat. ' ,
'k. All of the above':'all'}

South = {'a. Geography':S_G,
         'b. Languages':'\n The Languages spoken in this region of India are - Telugu , Tamil , Kannada , Malayalam , English ',
         'c. Religions':'\n  The religions followed in this region are-Hinduism, Islam, Christianity',
         'd. Clothes':'\n South Indian women traditionally wear a sari, a garment that consists of a drape varying from 5 yards (4.6 m) to 9 yards (8.2 m) in length and 2 feet (0.61 m) to 4 feet (1.2 m) in breadth that is typically wrapped around the waist, with one end draped over the shoulder, baring the midriff.\n The sari is to be wrapped around the waist, with the loose end of the drape to be worn over the shoulder, baring the midriff as according to Indian philosophy, the navel is considered as the source of life and creativity. Madisar is a typical style worn by Brahmin ladies from Tamil Nadu.\n Women wear colourful silk sarees on special occasions such as marriages.\n The men wear a dhoti, a 4.5 metres (15 ft) long, white rectangular piece of non-stitched cloth often bordered in brightly coloured stripes. It is usually wrapped around the waist and the legs and knotted at the waist.\n A colourful lungi with typical batik patterns is the most common form of male attire in the countryside.\n People in urban areas generally wear tailored clothing and western dress is popular in urban areas.Western-style school uniforms are worn by both boys and girls in schools even in rural areas.',
         'e. Food':'\n Rice is the staple diet, while fish is an integral component of coastal South Indian meals.Coconut and spices are used extensively in South Indian cuisine. The region has a rich cuisine involving both traditional non-vegetarian and vegetarian dishes comprising rice, legumes and lentils. Its distinct aroma and flavour is achieved by the blending of flavourings and spices including curry leaves, mustard seeds, coriander, ginger, garlic, chili, pepper, cinnamon, cloves, green cardamom, cumin, nutmeg, coconut and rosewater.\n The traditional way of eating a meal involves being seated on the floor, having the food served on a banana leaf and using clean fingers of the right hand to take the food into the mouth. After the meal, the fingers are washed; the easily degradable banana leaf is discarded or becomes fodder for cattle. \n Eating on banana leaves is a custom thousands of years old, imparts a unique flavor to the food and is considered healthy. Idli, dosa, uthappam, Pesarattu, appam, pongal and paniyaram are popular dishes for breakfast in states of Tamil Nadu, Andhra Pradesh and Kerala.\n Rice is served with sambar, rasam and poriyal for lunch. Andhra prasesh cuisine is characterised by pickles and spicy curries.   Famous dishes of Andhra cuisine are Pesarattu,Ulava charu, Bobbatlu, Putharekulu and Gongura.\n Chettinad cuisine is famous for non-vegetarian items and Hyderabadi cuisine is popular for its biryani.',
         'f. Festivals':S_festivals,
         'g. Heritage sites':S_hs,
         'h. Literature':'\n South India has an independent literary tradition dating back over 2500 years. The first known literature of South India is the poetic Sangam literature, written in Tamil 2500 to 2100 years ago. The literature was composed in three successive poetic assemblies known as Tamil Sangams that were held in the ancient times on a now vanished continent far to the south of India. This literature includes the oldest grammar treatise Tholkappiyam and epics Silappatikaram and Manimekalai written in Tamil.References to Kannada literature appear from fourth century CE.  Telugu literature adopted a form of Prakrit which in course of development became the immediate ancestor of Telugu. Poets like Annamacharya made many contributions to Telugu literature. Distinct Malayalam literature came later in the 13th century.',
         'i. Music':'\n The traditional music of South India is known as Carnatic music, which includes rhythmic and structured music by composers like Purandara Dasa, Kanaka Dasa, Tyagayya, Annamacharya, Bhakta Ramadasu, Muthuswami Dikshitar, Shyama Shastri, Kshetrayya, Mysore Vasudevachar and Swathi Thirunal.\n The main instrument that is used in South Indian Hindu temples is the nadaswaram, a reed instrument played along with thavil, a type of drum instrument to create an ensemble.\n The motion picture industry has emerged as an important platform in South India over the years, portraying the cultural changes, trends, aspirations and developments experienced by its people. \n South India is home to several distinct dance forms such as Bharatanatyam, Kuchipudi,Andhra Natyam,Kathakali, Kerala Natanam, Koodiyattam, Margamkali, Mohiniaattam, Oppana, Ottamthullal, Theyyam, Vilasini Natyam and Yakshagana.\n The dance, clothing and sculptures of South India exemplify the beauty of the body and motherhood.',
         'j. Dance': '\n Kuttiyattam Dance, Kerala – The theme of the Kuttiyattam dance is mythology. Kuttiyattam means acting together and that is the essence of this traditional dance form.\n The stage is taken over by 2-3 performers who recite verses in Sanskrit language.\n Kummi Dance, Tamil Nadu – Danced by women, the Kummi dance has its roots in Tamil Nadu. The women come together in a circle and dance while clapping their hands.\n Dollu Kunitha Dance, Karnataka – Also known as the “Drum Dance”, the Dollu Kunitha is a popular folk dance from Karnataka. During the dance, men beat the drums which they carry around their neck. The drum is highly decorated and is used to play strong beats.\n Some of the other Tribal dances from South of India include Dandaria Dance, Karagam Dance, etc.' ,
         'k. All of the above':'all'}

East = {'a. Geography':' \n East India is a region of India consisting of the Indian states of Bihar, Jharkhand,  Odisha and West Bengal',
'b. Languages':'\n Bengali language is spoken in West Bengal;Oriya language is used in Orrisa;Bhojpuri and Hindi Language is predominant in Bihar state',
'c. Religions':'\n The religions followed in this region are- Hindu, Muslim, Christian, other tribal religions',
'd. Clothes':'\n West Bengal -\n West Bengal is a state of extremely rich culture and history. Every corner of the streets of West Bengal has a story to share. Not only has this land given us some of the most renowned names in the country, it also happens to be a place of strong civilisation.,\n The costume of West Bengal is known for its distinct features and is perhaps the most popular example of our culture.The traditional dress of Bengali men is dhoti. The top or kurta that is paired with dhoti is called panjabi.In earlier times and especially during British Era, the dhotis were synonymous with white color. However, these days, to add a twist to the attire the dhoti is made available in number of attractive colors.The kurtas are usually made of silk or cotton and run up to knee length.The lungi happens to be another variation of the men’s costume. However that is more of an informal casual indoor wear.\n Saree is the signature traditional attire for the women in West Bengal. The saree captures the very essence of the culturally infused state West Bengal is. Even the saree draping style of Bengali women is quite distinct and has become more of a distinguishing feature now. Sarees are primarily woven in cotton and silk which have been named chiefly after their weaving techniques. The traditional weavers or Tantis of West Bengal are reputed worldwide because of the quality of fabric spun and their elaborate thread work. In various districts of Bengal like Murshidabad, Malda, Nadia, Birbhum, Bankura and Hooghly, different varieties of Sarees are woven with supreme efficiency and dedication.\n Clothes worn in orissa \n In Odisha, women wear different types of saris, which makes for glowing the beauty of women. Odisha is famous for Kataki Sari and Sambalpuri Sari. These sari designs contain very peculiar designs and seem very dignified Most of the women in Odisha interested in wearing these saris during festival occasions, Marriage occasions and other auspicious days. Shalwar Kameez is famous costumes in India, here the girls also interest to the Shalwar Kameez. Some tribal people also living in some areas in Odisha, they have some variety of dresses to wear. Hence most of the women in Odisha interest to beautify themselves by wearing valuable jewelry, fancy ornaments, and much other decorative jewellery. \n In Odisha, Men is interesting to wear their own traditional outfits. Generally, Dhoti is common traditional costumes for men in Odisha. They also wear Kurta and Gamucha during the festival and other traditional celebrations.',
'e. Food':'\n West Bengal\n Bengali cuisine is a culinary style originating in Bengal which is now divided between the Indian state of West Bengal and today\'s Bangladesh. Other regions, such as Tripura, and the Barak Valley region of Assam (in India) including some parts of Jharkhand and Bihar also have large native Bengali populations and share this cuisine. With an emphasis on fish, vegetables and lentils served with rice as a staple diet, Bengali cuisine is known for its subtle (yet sometimes fiery) flavours, and its huge spread of confectioneries and desserts. It also has the only traditionally developed multi-course tradition from the Indian subcontinent that is analogous in structure to the modern service à la russe style of French cuisine, with food served course-wise rather than all at once.\nBengali food has inherited a large number of influences, both foreign and pan-Indian, arising from a historical and strong trade links with many parts of the world. Bengal fell under the sway of various Turkic rulers from the early thirteenth century onwards, and was then governed by the British for two centuries (1757–1947).\nOdisha\nOdia cuisine refers to the cooking of the eastern Indian state of Odisha. Foods from this area are rich and varied, while relying heavily on local ingredients. The flavours are usually subtle and delicately spiced, quite unlike the fiery curries typically associated with Indian cuisine. Fish and other seafood such as crab and shrimp are very popular. Chicken and mutton are also consumed, but somewhat occasionally. Only 6% of the population of Odisha is vegetarian, and this is reflected in its cuisine. The oil base used is mostly mustard oil, but in festivals ghee is used. Panch phutana, a mix of cumin, mustard, fennel, fenugreek and kalonji (nigella) is widely used for tempering vegetables and dals, while garam masala (curry powder) and haladi (turmeric) are commonly used for non-vegetarian curries. Pakhala, a dish made of rice, water, and yogurt, that is fermented overnight, is very popular in summer, particularly in the rural areas. Oriyas are very fond of sweets and no Oriya repast is considered complete without some dessert at the end. Festivals and fasts witness a cuisine without onion and garlic, whereas other days witness an aroma of garlic and onion paste in curries. One can find restaurants serving food without onion and garlic in major places like Puri and other coastal area, which is run by Brahmin owners.\nOdisha has a culinary tradition spanning centuries if not millennia. The kitchen of the famous Jagannath temple in Puri is reputed to be the largest in the world, with a thousand cooks, working around 752 wood-burning clay hearths called chulas, to feed over 10,000 people everyday\nBihar\nThe cuisine of Bihar is largely similar to North indian cuisine and East Indian cuisines (for example Bengali cuisine). It is highly seasonal; watery foods such as watermelon and sharbat made from the pulp of the wood-apple fruit are consumed mainly in the summer months, while dry foods such as preparations made of sesame seeds and poppy seeds are consumed more frequently in the winter months.\nThere are numerous Bihari meat dishes, with chicken and mutton being the most common. Fish dishes are especially common in the Mithila region of North Bihar due to the number of rivers, such as the Sone, Gandak, Ganges and Koshi. Dairy products are consumed frequently throughout the year, including dahi (yogurt), spiced buttermilk (known as mattha), ghee, lassi and butter.\nDishes for which Bihar is famous include Bihari kebabs, litti chokha, Bihari boti, Bihari chicken masala, sattu paratha (parathas stuffed with roasted gram flour), chokha (spicy mashed eggplant and potatoes), fish curry and posta-dana ka halwa.',
'f. Festivals':E_festivals,
'g. Heritage sites':E_hs,
'h. Literature': '\n West Bengal has a rich legacy of amazing literature with great authors like Sharat Chandra Chattopadhyay, Rabindranath Tagore, Kazi Nazrul Islam and Bankim Chandra Chattopadhyay contributing their fair share to the Bengali literature as well as to the world literature.\n In the pre-Sarala period, Natha and Siddha literature flourished in Odisha. The main works of this period are Shishu veda (an anthology of 24 dohas), Amara Kosha and Gorakha Samhita. Shishu veda is mentioned in the works of Sarala Das and the later 16th century poets. It is written in Dandi brutta.\n In the field of literature, Bihar has produced a number of writers in its regional languages like Bhojpuri Maithili language, Magahi language, Angika and Bajjika including Bhikhari Thakur, Heera Dom, Viveki Rai, Satishwar Sahay Verma etc are writers of Bhojpuri, Vidyapati in maithilli.' ,
'i. Music':'\n Music of West Bengal - \nRabindra Sangeet, also known as Tagore Songs, are songs written and composed by Rabindranath Tagore. They have distinctive characteristics in the music of Bengal, popular in India and Bangladesh. "Sangeet" means music, "Rabindra Sangeet" means Songs of Rabindra.\nRabindra Sangeet used Indian classical music and traditional folk music as sources.Tagore wrote some 2,230 songs.\nRabindranath Tagore was a towering figure in Indian music. Writing in Bengali, he created a library of over 2,000 songs now known by Bengalis as rabindra sangeet whose form is primarily influenced by Hindustani classical, sub-classicals, Karnatic, western, bauls, bhatiyali and different folk songs of India. Many singers in West Bengal and Bangladesh base their entire careers on the singing of Tagore musical masterpieces. The national anthem of India and national anthem of Bangladesh are Rabindra Sangeets.\n West Bengal\'s capital Kolkata is also the cultural capital of India.\n Panchali is a form of narrative folk songs of the Indian state of West Bengal. The word Panchali probably originates from panchal or panchalika, meaning puppet. According to another school of that, Panchali originates from the word panch, which means five in Bengali language, referring to the five elements of this genre: song, music, extempore versifying, poetic contests, and dance.\n Music of Odisha\nOdissi music is a classical music in India originated from the eastern state of Odisha. Indian Classical music has five significant branches: Avanti, Panchali, Udramagadhi, Hindustani and carnatic. Of these, Udramagadhi exists in the form of Odissi music.Generally, Odissi is one of the classical dances of India performed with Odissi music. Odissi music got shaped during the time of famous Oriya poet, Jayadeva, who composed lyrics meant to be sung. By the 11th century CE folk music of Odisha existing in the form of Triswari, Chatuhswari, and Panchaswari was modified into the classical style. However, Odissi songs were written even before the Odia language developed. Odissi music has a rich legacy dating back to the 2nd century BCE, when king Kharvela, the ruler of Odisha (Kalinga) patronised this music and dance.\n Like Hindustani and Carnatic systems, Odissi music is a separate system of Indian classical music and is having all the essential as well as potential ingredients of Indian Classical form. But it has not come to limelight due to apathy from the time of British rule in Odisha, want of its proper study, revival, propagation, etc. Despite the fact, the traditional music form could be saved and maintained in its pristine form. Thanks to the musicians particularly of Jaga Akhadas of Puri district, who could develop and maintain the music. The music movement of Odisha, however, took a different turn after independence.\n Like other aspects of her culture, music of the sacred land (Odisha) is charming, colourful, variegated encompassing various types. The existing musical tradition of Odisha, the cumulative experience of the last two thousand five hundred years if not more, can broadly be grouped under five categories such as: (1) Tribal Music, (2) Folk Music, (3) Light Music, (4) Light-Classical Music, (5) Classical Music, which need a short elucidations for better understanding the subject in all India context.\n The tribal music as the title signifies is confined to the tribals living mainly in the hilly and jungle regions and sparsely in the coastal belt of Odisha. Odisha has the third largest concentration of tribes constituting about one fourth of the total population. They are distributed over 62 tribal communities.\n Odisha is the treasure house of Folk Songs which are sung on different festivals and specific occasions in their enjoyment. Folk music in general is the expression of the ethos and mores of the folk communities. Of the bewildering variety of folk music of Odisha, mention may be made of Geeta, Balipuja Geeta, Kela Keluni Geeta, Dalkhai Geeta, Kendra Geeta, Jaiphula Geeta, Ghumura Geeta, Ghoda Nacha and Danda Nacha Geeta, Gopal Ugala and Osa-Parva-Geeta etc.\n Bhajan, Janan, Oriya songs based on ragas, Rangila Chaupadi etc. are grouped under Light classical music, which forms an important segment of Oriya music. Sri Geetagovinda, Anirjukta Pravadha, Divya Manusi Prabandha, Chautisa, Chhanda, Chaupadi (now known as Odissi), Champu, Malasri, Sariman, nVyanjani, Chaturang, Tribhang, Kuduka Geeta, Laxana and Swaramalika are the various sub-forms, which individually or collectively constitute the traditional Odissi music. These sub-forms of the traditional Odissi music, can be categorised under the classical music of Odisha.',
'j. Dance':'\n Odissi (Odissi) is a classical dance in Eastern India. It originates from the state of Odisha, in Eastern India. It is the oldest surviving dance form of India based on archaeological evidences. Odissi has a long, unbroken tradition of 2,000 years and finds mention in the Natyashastra of Bharatamuni, possibly written circa 200 BCE.\n Mahari Dance is one of the important dance forms of Odisha and originated in the temples of Odisha. History of Odisha provides evidence of the \'Devadasi\' cult in Odisha. Devadasis were dancing girls who were dedicated to the temples of Odisha. The Devadasis in Odisha were known as \'Maharis\' and the dance performed by them came to be known as Mahari Dance. \n Gotipua dance is another form of dance in Odisha. In Oriya colloquial language Gotipua means a single boy. The dance performance done by a single boy is known as Gotipua dance.\n There are many folk dances in east India, with the best-known being Jhijhiya, Jhumair, Domkach, Ghumura Dance, Sambalpuri and Chhau dance.Jhijhiya is a cultural dance from the Mithila region. Jhijhiya is mostly performed at time of Dusshera, in dedication to Durga Bhairavi, the goddess of victory. While performing jhijhiya, women put lanterns made of clay on their heads and they balance it while they dance. Jhumair is a folk dance in Chota Nagpur Plateau region of Jharkhand, Chhattisgarh, Odisha and West Bengal. It is performed during harvest season and festivals accompanied by musical instruments such as Madal, Dhol, Bansuri, Nagara, Dhak, and Shehnai. Domkach is a folk dance in the state of Bihar, Jharkhand, Chhattisgarh and Odisha. It performed during marriage in the house of Bride and groom.\n Chhau is a form of tribal martial dance popular in the Indian states of West Bengal, Jharkhand and Odisha. There are three regional variations of the dance. Seraikella Chau was developed in Seraikella, the administrative head of the Seraikela Kharsawan district of Jharkhand; Purulia Chau in Purulia district of West Bengal; and Mayurbhanj Chau in Mayurbhanj district of Odisha. Ghumura Dance Archaeological evidence shows cave paintings from the pre-historic period discovered by Gudahandi of Kalahandi and Yogi Matha of Nuapada district that represent the Ghumura and Damru, among other instruments. These paintings date to as early as 8000 BCE and from such painting the antiquity of musical instrument Ghumura and Damru can be imagined. The origin of Ghumura goes back to ancient times. There is a beautiful waterfall in the river valley of Indravati which was initially recognised by Chindak Naagas of Chakrakot. Many believe that Ghumura dance originated from this river valley and gradually spread into the areas between Indravati and Mahanadi, indicating this dance form belongs to the 10th century CE.\n The western Odisha has also great variety of dance forms unique to Odisha culture. The children\'s verses are known as "Chhiollai", "Humobauli" and "Dauligit". The adolescent poems are "Sajani", "Chhata", "Daika", "Bhekani". The eternal youth composes "Rasarkeli", "Jaiphul", "Maila Jada", "Bayamana", "Gunchikuta" and "Dalkhai". The work-man\'s poetry comprises "Karma" and "Jhumer", both pertaining to Lord Vishwakarma and the "Karamashani" goddess.\n The professional entertainers perform Dand, Danggada, Mudgada, Ghumra, Sadhana, Sabar – Sabaren, Disdigo, Nachina – Bajnia, Samparda and Sanchar. They are performed on a variety of occasions and their rhymes and rhythms change accordingly.Bengali dance forms draw from folk traditions, especially those of the tribal groups, as well as from the broader Indian dance tradition. Dance forms of Bihar are another expression of rich traditions and ethnic identity.  There are several folk dance forms that can keep one enthralled, such as dhobi nach, jhumarnach, manjhi, gondnach, jitiyanach, more morni, dom-domin, bhuiababa, rah baba, kathghorwa nach, jat jatin, launda nach, bamar nach, jharni, jhijhia, natua nach, bidapad nach, sohrai nach and gond nach.',
'k. All of the above':'all'}

West = {'a. Geography':W_G,
'b. Languages':'\n  The languages spoken in this region are-Gujarati ,Kannada, Konkani, Marathi, Hindi, English',
'c. Religions':'\n The religions followed in this region are- Hindu, Muslims, Jains, islam, Buddhism, Christianity, and Sikhism. ',
'd. Clothes':'\n Madhya Pradesh, Gujarat dress -\n The traditional dress of Indian women in these states is the colourful ghagra choli. The choli is brightly embroidered, waist-length bare-backed blouses. Ghagras or lehengas are gathered ankle-length skirts secured around the waist. The attire is completed by an odhni or dupatta draped across the neck or over the head. Saree is also another traditional dress of Gujarat but here the pallu is draped in front rather than over the shoulders\n Maharashtra Attire -\n Sari is the traditional garment here worn in distinctive Maharashtrian style. In Maharashtra, the sari is 9 metre long and is worn tucked between the legs. This saree does not require a petticoat or a slip. The famous Paithani sari is worn by Maharashtrian women during festivals and religious functions.\n Goa Attire-\n Goans are very much fashion aware and tourists are likely to see the very latest designer wear on the streets, no sooner than the it appears elsewhere in India. Clothes form an important part of the Goan lifestyle making it essential to dress well at the innumerable social occasions that occur around the year. Western dresses like skirts and tops, trousers and shirts, wrap-arounds are preferred by women in Goa. Goan Christian women still wear sarees rather than dresses. There is a visible presence of western, particularly Portuguese, influence evident in the style of houses, churches, dress and cuisine in Goa.',
'e. Food':'\n The cuisine of Western India is diverse. Surat City Of Gujarat is Worldwide Known For Food, Maharashtrian cuisine is diverse and ranges from bland to fiery hot. Pohay, Shrikhand, Pav Bhaji, Vada Pav are good examples of Maharashtrian cuisine. \n Goan cuisine --is dominated by the use of rice, coconut, seafood, Kokum, cashew-nuts. With its distinct spices and medium of cooking as coconut oil, both vegetarian as well as non-vegetarian cuisine is equally popular. \n Gujarati cuisine-- is almost exclusively vegetarian. Gujarat is one of three states in India, with prohibition on alcohol, along with Mizoram and Manipur. In contrast, Maharashtra has some of the best vineyards in India, with Nashik and Sangli districts being the country\'s biggest grape-producing districts.',
'f. Festivals':'\n Festivals of Maharashtra-\n  Ganesh Chaturthi is the grand festival of Maharashtra. It is however also celebrated in other states of India with great fervour. Vinayaka Chaturthi is another name for this festival. This festival is celebrated in the honour of Lord Ganesha, the son of Lord Shiva and Parvati. Lord Ganesha is believed to bestow prosperity, wisdom and fortune.   Elephanta Festival is another important festival which is celebrated on the Elephanta Island, in the month of February. A musical tribute to Lord Rama is paid through the Banganga festival in Mumbai. The festival is accompanied by musical carnival and promotes the cultural heritage of the state. Ellora festival is another festival which celebrates the classical dance and music of Maharashtra at the Ellora caves.    Shivaji Jayanti is celebrated in the honour of the greatest ruler of the state, on the birthday of Chatrapati Shivaji Maharaj. Other festivals of Maharashtra include Bhaubeej, Ganga Dashahara, Jiviti Puja, Kalidas Festival, Kojagiri Purnima, Maharashtra Day, Nagpanchami, Narali Poornima, Palkhi Festival, Pola Festival and Vat Purnima. \n Festivals of Gujarat -\n Among the festivals of Gujarat, International Kite Festival is a significant one. On 14th of January, Makar Sankranti, this festival is celebrated by flying kites throughout the state. This festival also marks the end of winter and some of the exclusive kites flown in the Kite Festival are the manifestation of skilled artistry. In the month of February and March, Kutch Mahotsav is celebrated. It aims at promoting the tourism of Kutch and attracts tourists from different regions to witness the beautiful handicrafts, historical towns and the colourful culture and traditions of Gujarat. Navaratri is one of the most popular festivals of Gujarat and is celebrated since ancient times. Navaratri is celebrated for nine days in the honour of Mother Goddess who is believed to protect her devotees. Traditional dances like Garba, Dandia and Bhavai are the most prominent features of this festival. Saptak Music Festival is celebrated in Ahmedabad in the month of January. The festival focuses on the promotion of Indian classical music of India and was inaugurated by the legendary musician Pandit Ravi Shankar in year 1980. Talented musicians from different parts of India give extraordinary performances in Saptak School of Music, during this eleven day celebration. In January, Modhera Dance Festival is organized in the Sun Temple of Modhera. Amazing classical dance performances make this festival worth experiencing. Holi, Raksha Bandhan, Janmashtami and Diwali are enlisted among the important festivals of Gujarat. \n Festivals of Goa -\n Great celebrations of different festivals can also be witnessed in Goa. Shigmo is a colourful festival of Goa. Exquisite folk dances by various dance troupes are the most alluring features of this festival. Goa Heritage Festival at Fontainhas is celebrated with the aim of preserving and promoting the Fontainhas area in Goa. It is a beautiful celebration of the cultural heritage of Goa. Grandest celebration and cultural extravaganza is organized in the Goa Carnival. The four day carnival is accompanied by extraordinary folk dances and music. In Goa, Christmas is also celebrated with great vigour where the state is beautifully adorned and illuminated. Sao Joao festival marks the beginning of the monsoon in Goa. This festival is the celebration of the feast of St. John the Baptist. It is a colourful festival exhibiting unique traditions of Goa. Apart from this, festivals like Dussehra, Diwali and Holi are also celebrated with great zeal in Goa.',
        'g. Heritage sites':W_hs,
        'h. Literature':'\n Literature in Gujarat stands for its Literary tradition in the form of folk songs, narratives, theater and aphorisms. Traced back to the Sultanate period, the stories and messages evolved as they passed through generations, leaving behind versions of myth and legends.\n Rajasthani literature written in various genres starting from 1000 AD. But, it is generally agreed that modern Rajasthani literature began with the works of Surajmal Misrana. His most important works are the Vansa Bhaskara and the Vir Satsai.\n Marathi literature is the body of literature of Marathi, an Indo-Aryan language spoken mainly in the Indian state of Maharashtra and written in the Devanagari and Modi script.',
        'i. Music':'\n Gujarati folk music consists of a wide variety. Bhajan, a devotional song type poetry are categorized by theme of poetry/lyrics and by musical compositions such as Prabhati, Katari, Dhol etc. The Bard traditions of Barot, Charan and Gadhvi communities has preserved and enriched the folk tradition of story telling with or without music. This includes the forms of Doha, Sorathaa, Chhand, etc. \n The songs and music accompanying traditional dance forms such as Garba, Dandiya Raas, Padhar, Dangi and Tippani are unique in nature.\n Rajasthan has a diverse collection of musician castes, including langas, sapera, bhopa, jogi and Manganiar. There are two traditional classes of musicians: the Langas, who stuck mostly exclusively to Muslim audiences and styles, and the Manganiars, who had a more liberal approach. Traditional music includes the women\'s Panihari songs, which lyrically describes chores, especially centered on water and wells, both of which are an integral part of Rajasthan\'s desert culture\n  folk music in Maharashtra include Bhajan, Bharud, Gondhal, Kirtan, Lalita, Abhangas and Tumbadi, Gondhal, Lalita, Lavani, Povadas',
        'j. Dance': '\n Garba Dance, Gujrat – The Garba dance is extremely well known and is performed by women in Gujrat, especially during the Navratras.\n The women dance in circles while holding earthen pots on their heads. While dancing, the women clap their hands and click their fingers.\n  The burning oil lamp placed within the pot signifies embryonic life.\n Jawar Dance, Madhya Pradesh – This harvest dance is a favourite of the farmers, especially in Madhya Pradesh’s Bundelkhand region. \n After a good harvest, farmers rejoice by performing this dance. The women are known to carry baskets of jawar on their heads while dancing to the tune of several musical instruments, percussion instruments and stringed instruments \n Bhagoriya Dance, Madhya Pradesh – The Bhils tribe of MP perform this lyrical dance, mainly during the Indian festival of Holi.\n Dandiya Dance, Gujrat – Men and women perform the dandiya dance together. The most distinguishing feature of this dance is that dancers hold sticks in their hands and while beating these sticks on their own and with other dancers on either side, they move round in circles. \n During the dance, dancers take various positions such as standing, sitting, etc. Dandiya raas becomes extremely colourful when the dancers dress up in multi colored outfits. \n Mando Dance, Goa – Among the various folk dances of Goa such as Jagar, Dekhni and Suvari, etc, the Mando is quite well known. A semi-urban folk dance, the Mando is performed at a speed that progresses gradually.' ,
        'k. All of the above':'all'}
North_east = {'a. Geography':NE_G,
              'b. Languages':'\n The languages spoken in this region are-Bodo, Khasi, Garo, Assamse, Manipuri (Maiteis) etc. ',
              'c. Religions':'\n The religions followed in this region are-Christians, tribal religions, Hindus',
              'd. Clothes':'\n North-East India, also called the Seven Sister States of India is famous for its link with the culture and tradition of ancient times. Each state of this region has traditional attires, which reciprocates the beauty of the culture with designs and colors crafted for specific social status. Find below about Traditional dresses of North East India.\n  Nagaland \n The traditional dress of Nagaland is Li. This style of dressing has numerous patterns and designs, especially embroidered. They wear a phanek below the waist, which is similar to a low skirt. Mechala is the common upper wear. It is a wraparound shirt.The shawls of the dress have more work done to it. The shawls of grand work are worn by people of higher class. Usually, the designs are geometric shapes and floral patterns. \n  Meghalaya \nThe Khasi is also called Jainse or Dhara. This style of attire is worn by women and is paired with heavy silver accessories. They wear a cylindrical lower waist cloth and cover up with a bright yellow shawl. Men wear loin cloth with a jacket. Turban or any headgear is common. \n Manipur \n This is quite similar to Khasi. However, the shawl is usually made of silk, named Innaphi.  Wrapped shirt with phanekand shawl is the common dresses for women. Men wear dhoti with jacket and white turban. Their dresses have simple embroidery and different occasions call for different color attire. \n Arunachal Pradesh\n Each tribe in Arunachal Pradesh has a different style of clothing. The basic style of dress is chemise, which is a sleeveless shirt with a full sleeved jacket, which is embroidered. They wear a skirt, which looks like a wrapped-around loin cloth. Skull cap made with Yak hair is the famous accessory among men.\n Tripura\n The lower part is called Raignai and the dress covering the chest region is called Risa, and the upper dress is Rikutu. All the three pieces are well decorated. Men wear a towel and shirt with turban. However, this style of dressing is diminishing.\n Assam\n The traditional dress for women is a wrapped around skirt with a sari pallu on the top. They have different style of patterns and colors, but those have no correlation with the social statue or style of occasion. Men wear a dhoti or loin cloth around their waist, up to their ankles and wear a chadar on top. \n  Mizoram \n Mizoram’s traditional dress is quite different than the others. They wear a skirt with vertical embroidery and a full-sleeve top. This is the festive attire in this region. Men wear loose trousers with a leather belt.',
              'e. Food':'\n Arunachal Pradesh-\n Rice, fish, meat, leaf vegetables\n Thukpa, momo, apong (rice beer)\n Assam Cuisine -\n Assam tea, Pitha, khar, tenga, pura, tamul (betel nut) – paan, rice beer\n Manipur Cuisine -\n Eromba, u-morok, singju, ngari (fermented fish), kangshoi\n Nagaland Cuisine-\n fermented bamboo shoot, smoked pork and beef, axone, bhut jolokia\n Sikkim Cuisine - \n Thukpa, momo, sha Phaley, gundruk, sinki, sel roti\n Mizoram Cuisine --\n Bai, bekang (fermented soya beans), sa-um (fermented pork), sawhchiar\n Meghalaya Cuisine --\n Jadoh, ki kpu, minil, nakham (dried fish), momo, bamboo shoot',
              'f. Festivals':NE_festivals,
              'g. Heritage sites':'\n 1. The Darjeeling Himalayan Railway, Darjeeling-an elegant ride:-\n Also known as “Toy Train”, is one of gorgeous heritage sited in West Bengal.\n Since 1999 the train has been declared as a World Heritage Site by UNESCO. In 2005, UNESCO added the Nilgiri Mountain Railway as an extension to this. In 2008 the 96-kilometer, 2.5-foot gauge Kalka–Shimla Railway, was also added to it.\n 2. Khangchendzonga National Park, Sikkim-hub of biodiversity:-\n The Khangchendzonga National Park of Sikkim is a real treat for nature lovers.This park is stated as one of the famous heritage sites for its alluring biodiversity.\n The park gets its name from the third highest peak in the world, Mount Khangchendzonga, and also for an array of natural wonders such as caves, rivers, lakes, and forests around here. One should explore this national park for experiencing its natural wonder.\n 3. Jowai, Meghalaya- ‘City of scenic beauty’:-\n Jowai, a city of Jaintia Hills district, is famous for picturesque views with the perfect mix of heritage and culture.\n The main attraction of this place is Thadlaskein Lake. Lalong Park is another famous tourist’s hot spot.\n It is known for Unokotiswara Kal Bhairava\n 4. Guwahati, Assam- “The gateway to the North-East”:-\n Guwahati, a charming city, serves as the gateway to the Seven Sisters of North East India. It is not only home to age-old temples which will take you centuries back of ancient history, but it also boasts of a modern lifestyle along with an electric nightlife.\n The peaceful ambiance in the city is one of the main reasons you should visit Guwahati once in a lifetime.\nIt is Known for: Kamakhya Temple, Umananda Temple, and Guwahati Zoo\n5. Imphal, Manipur-“The site of Battle of Imphal”:-\nIt is another famous heritage sites in the North-Eastern for its sceneries, charming landscapes as well as a significant history that will give the hints of the past around the city.\nThe lush green landscapes, an alluring ambiance, and serene rivers make Imphal an ideal tourist destination. This place has a historical importance because of World-War II. Some of the famous attractions are\n-Manipur State Museum,\n-Kangla Fort,\n-Langthabal, war cemeteries,\n-Loktal Lake,\n-Keibul Lamjao National park.\nImphal is Known for: Loktak Lake, Sendra Island, Kangla Fort, and Shaheed Minar',
              'h. Dance':'\n Arunachal Pradesh\n Wancho dances, Idu Mishmi dance, Digaru Mishmi Buiya dance, Khampti dance, Ponung dance, Sadinuktso\n Assam\n Sattriya, Bagurumba, Bihu dance, Bhaona (For more see Music of Assam)\n Manipur\n Manipuri dance (Ras Lila), Kartal Cholom, Manjira Cholom, Khubak Eshei, Pung Cholom, Lai-Haraoba',
              'i. Music':'\n Northeast is a hub of different genres of music. Each community has its own rich heritage of folk music. Talented musicians and singers are plentifully found in this part of the country. The Assamese singer-composer Bhupen Hazarika achieved national and international fame with his remarkable creations. Another famous singer from Assam, Pratima Barua Pandey is a well-known folk singer. Zubeen Garg, Papon, Anurag Saikia are some other notable singers, musicians from the state of Assam. Tangkhul Naga folk blue singer like Rewben Mashangva, who comes from Ukhrul, is an acclaimed Folk singer whose music is inspired by the like of Bob Dylan and Bob Marley. Another famous folk singing band from Nagaland popularly known as Tetseo Sisters is one to be noted for their original music genre. However, younger generation has started pursuing western music more and more nowadays. Northeast is witnessing immense rise of musical revolution in the 21st century',
              'j. Literature':'\n Many of the Northeast Indian indigenous communities have an ancient heritage of folktales which tell the tale of their origin, rituals, beliefs and so on. These tales are transmitted from one generation to another in oral form. They are remarkable instances of tribal wisdom and imagination. However, Assam and Manipur have some ancient written texts. These states were mentioned in the great Hindu epic Mahabharata. The Saptakanda Ramayana in Assamese by Madhava Kandali is considered the first translation of the Sanskrit Ramayana into a modern Indo-Aryan Language. Karbi Ramayana bears witness to the old heritage of written literature in Assam. Two writers from the Northeast, viz., Birendra Kumar Bhattacharya and Mamoni Raisom Goswami, have been awarded Jnanpith, the highest literary award in India.[67] Hence, Birendra Kumar Bhattacharya was the first Assamese writer and from the Northeast India to receive Jnanpith Award for his Assamese novel Mrityunjay(1979).[68] Mamoni Raisom Goswami was awarded the Jnanpith Award in the year 2000. Nagen Saikia is the first writer from Assam and the Northeast India, to have been conferred the prestigious Sahitya Akademi Fellowship by the Sahitya Akademi. The last quarter of the 20th century saw the rise of modern literature in the Northeast. Most of the writers, especially the tribal writers, are bilingual, that is, they write both in their mother-tongue and English. Some of the general features of this literature are—retrieval of folklore, celebration of folk culture, identity politics, reaction to the insurgency and counter-insurgency operations, depiction of natural beauty, changes meted out by time, etc. The major writers of Northeast Literature are--(from Assam) Lakshminath Bezbaroa, Homen Borgohain, Birendra Kumar Bhattacharya, Harekrishna Deka, Rongbong Terang, Nilmani Phukan, Indira Goswami, Hiren Bhattacharyya, Mitra Phukan, Jahnavi Barua, Dhruba Hazarika, Rita Chowdhury, D N Bezbarua, Nilim Kumar, Anupama Basumatary, Uddipana Goswami, Aruni Kashyap; (from Arunachal Pradesh) Mamang Dai; (from Manipur) Robin S Ngangom, Ratan Thiyam, Thangjam Ibopishak, Gambhini Devi, T Bijoykumar Singh; (from Meghalaya) Kynpham Sing Nongkynrih, Esther Syiem, Desmond Kharmawphlang, Paul Lyngdoh, Anjum Hassan; (from Mizoram) Mona Zote; (from Nagaland) Temsula Ao, Cherrie Chhangte, Easterine Kire; (from Sikkim) Sudha M Rai, Rajendra Bhandari (from Tripura) Chandrakanta Murasingh. Temsula Ao is the first writer from Northeast India to be awarded the Sahitya Akademi Award (2013) in the Indian English Literature category for her collection of short stories, Laburnum for My Head, and Padmashree (2007). Easterine Kire is the first English novelist hailed from Nagaland. She received The Hindu Literary Prize (2015) for her novel When the River Sleeps. Indira Goswami, alias Mamoni Roisom Goswami, is an acclaimed Assamese writer whose novels include Moth-Eaten Howda of the Tusker, Pages Stained with Blood, The Shadow of Kamakhya and The Blue-Necked God. Mamang Dai won the Sahitya Akademi Award (2017) for her novel The Black Hill.',
              'k. All of the above':'all'}
#Main
def Main():
    #choice of region
    print('These are the Regions of India-: ')
    s = gTTS('These are the Regions of India-: ')
    s.save('one.mp3')
    playsound('one.mp3')
    for i in Regions:
        sleep(0.25)
        print('       '+i + " Region of India ")
        s = gTTS('       '+i + " Region of India ")
        s.save(i+'.mp3')
        playsound(i+'.mp3')
    sleep(0.5)
    ans=''
    answ = input('Which Region do you want know about?(Please only type 1 region and type North East without the space) ').lower()
    s = gTTS('Which Region do you want know about?')
    s.save('three.mp3')
    playsound('three.mp3')
    for i in answ.split(' '):
        if i == 'north' or i =='northern':
            ans='a'
        elif i == 'south' or i =='southern':
            ans='b'
        elif i == 'east' or i =='eastern':
            ans='d'
        elif i == 'west' or i =='western':
            ans='c'
        elif i == 'northeast' or i =='northeastern':
            ans='e'
            

    # North
    if ans == 'a':
        for key in North.keys():
            sleep(0.5)
            print(key, end='\n')
            s = gTTS(key)
            s.save(key+'.mp3')
            playsound(key+'.mp3')
        sleep(0.5)
        #choice of aspect
        answ= input('Which aspect do you want to learn about this region: ').lower()
        s = gTTS('Which aspect do you want to learn about this region:')
        s.save('five.mp3')
        playsound('five.mp3')
        for i in answ.split(' '):
            if i == 'geography':
                ans='a'
            elif i == 'language' or i =='languages':
                ans='b'
            elif i == 'religion' or i =='religions':
                ans='c'
            elif i == 'clothes':
                ans='d'
            elif i == 'food' or i=='eat':
                ans='e'
            elif i == 'heritage' or i=='monuments':
                ans='g'
            elif i == 'festivals':
                ans='f'
            elif i == 'music':
                ans='i'
            elif i == 'literature':
                ans='h'
            elif i == 'dance':
                ans='j'
            elif i == 'everything' or i == 'all':
                ans='k'
        if ans == 'a':
            #geographics
            sleep(0.5)
            for i in N_G.keys():
                print(i+"-: ", N_G[i] )
        elif ans == 'b':
            #languages
            sleep(0.5)
            print(North['b. Languages'])
        elif ans == 'c':
            #religions
            sleep(0.5)
            print(North['c. Religions'])
        elif ans == 'd':
            #clothes
            sleep(0.5)
            print(North['d. Clothes'])
        elif ans == 'e':
            #food
            sleep(0.5)
            print(North['e. Food'])
        elif ans == 'f':
            #festivals
            sleep(0.5)
            for i in N_festivals.keys():
                print(i+"-: ", N_festivals[i] )
        elif ans == 'g':
            #Heritage sites
            sleep(0.5)
            for i in N_hs.keys():
                print(i+"-: ", N_hs[i] )
        elif ans == 'h':
            #literature
            sleep(0.5)
            print(North['h. Literature'])
        elif ans == 'i':
            #music
            sleep(0.5)
            print(North['i. Music'])
        elif ans == 'j':
            #Dance
            sleep(0.5)
            print(North['j. Dance'])
        elif ans == 'k':
            #all
            sleep(0.5)
            print('\n Geography \n')
            for i in N_G.keys():
                print(i+"-: ", N_G[i] )
            print('\n Languages \n')
            print(North['b. Languages'])
            print('\n Religion \n')
            print(North['c. Religions'])
            print('\n Clothes \n')
            print(North['d. Clothes'])
            print('\n Food \n')
            print(North['e. Food'])
            print('\n Festival \n')
            for i in N_festivals.keys():
                print(i+"-: ", N_festivals[i] )
            print('\n Heritage Sites\n')
            for i in N_hs.keys():
                print(i+"-: ", N_hs[i] )
            print('\n Literature \n')
            print(North['h. Literature'])
            print('\n Music \n')
            print(North['i. Music'])
            print('\n Dance \n')
            print(North['j. Dance'])
        else:
            print('\n Please input the correct command ')
    

# south 
    elif ans == 'b':
        for key in South.keys():
            sleep(0.5)
            print(key, end='\n')
        sleep(0.5)
        #choice of aspect
        answ= input('Which aspect do you want to learn about this region: ').lower()
        for i in answ.split(' '):
            if i == 'geography':
                ans='a'
            elif i == 'language' or i =='languages':
                ans='b'
            elif i == 'religion' or i =='religions':
                ans='c'
            elif i == 'clothes':
                ans='d'
            elif i == 'food' or i=='eat':
                ans='e'
            elif i == 'heritage' or i=='monuments':
                ans='g'
            elif i == 'festivals':
                ans='f'
            elif i == 'music':
                ans='i'
            elif i == 'literature':
                ans='h'
            elif i == 'dance':
                ans='j'
            elif i == 'everything' or i == 'all':
                ans='k'
        if ans == 'a':
            #geographics
            sleep(0.5)
            for i in S_G.keys():
                print(i+"-: ", S_G[i] )
        elif ans == 'b':
             #languages
            sleep(0.5)
            print(South['b. Languages'])
        elif ans == 'c':
            #religions
            sleep(0.5)
            print(South['c. Religions'])
        elif ans == 'd':
            #clothes
            sleep(0.5)
            print(South['d. Clothes'])
        elif ans == 'e':
            #food
            sleep(0.5)
            print(South['e. Food'])
        elif ans == 'f':
            #festivals
            sleep(0.5)
            for i in S_festivals.keys():
                print(i+"-: ", S_festivals[i])
        elif ans == 'g':
            #Heritage sites
            sleep(0.5)
            for i in S_hs.keys():
                print(i+"-: ", S_hs[i] )
        elif ans == 'h':
            #literature
            sleep(0.5)
            print(South['h. Literature'])
        elif ans == 'i':
            #music
            sleep(0.5)
            print(South['i. Music'])
        elif ans == 'j':
            #Dance
            sleep(0.5)
            print(South['j. Dance'])
        elif ans == 'k':
             #all
            sleep(0.5)
            print('\n Geography \n')
            for i in S_G.keys():
                print(i+"-: ", S_G[i] )
            print('\n Languages \n')
            print(South['b. Languages'])
            print('\n Religion \n')
            print(South['c. Religions'])
            print('\n Clothes \n')
            print(South['d. Clothes'])
            print('\n Food \n')
            print(South['e. Food'])
            print('\n Festival \n')
            for i in S_festivals.keys():
                print(i+"-: ", S_festivals[i] )
            print('\n Heritage sites \n')
            for i in S_hs.keys():
                print(i+"-: ", S_hs[i] )
            print('\n Literature \n')
            print(South['h. Literature'])
            print('\n Music \n')
            print(South['i. Music'])
            print('\n Dance \n')
            print(South['j. Dance'])
        else:
             print('\n Please input the correct command ')
        


# West
    elif ans=='c':
        #choice of aspect
        for key in West.keys():
            sleep(0.5)
            print(key, end='\n')
        sleep(0.5)
        answ= input('Which aspect do you want to learn about this region: ').lower()
        for i in answ.split(' '):
            if i == 'geography':
                ans='a'
            elif i == 'language' or i =='languages':
                ans='b'
            elif i == 'religion' or i =='religions':
                ans='c'
            elif i == 'clothes':
                ans='d'
            elif i == 'food' or i=='eat':
                ans='e'
            elif i == 'heritage' or i=='monuments':
                ans='g'
            elif i == 'festivals':
                ans='f'
            elif i == 'music':
                ans='i'
            elif i == 'literature':
                ans='h'
            elif i == 'dance':
                ans='j'
            elif i == 'everything' or i == 'all':
                ans='k'
        if ans == 'a':
            #geographics
            sleep(0.5)
            for i in W_G.keys():
                print(i+"-: ", W_G[i] )
        elif ans == 'b':
             #languages
            sleep(0.5)
            print(West['b. Languages'])
        elif ans == 'c':
            #religions
            sleep(0.5)
            print(West['c. Religions'])
        elif ans == 'd':
            #clothes
            sleep(0.5)
            print(West['d. Clothes'])
        elif ans == 'e':
            #food
            sleep(0.5)
            print(West['e. Food'])
        elif ans == 'f':
            #festivals
            sleep(0.5)
            print(West['f. Festivals'])
        elif ans == 'g':
            #Heritage sites
            sleep(0.5)
            for i in W_hs.keys():
                print(i+"-: ", W_hs[i] )
        elif ans == 'h':
            #literature/craft
            sleep(0.5)
            print(West['h. Literature'])
        elif ans == 'i':
            #music
            sleep(0.5)
            print(West['i. Music'])
            
        elif ans == 'j':
            #Dance
            sleep(0.5)
            print(West['j. Dance'])
        elif ans == 'k':
             #all
            sleep(0.5)
            print('\n Geography \n')
            for i in W_G.keys():
                print(i+"-: ", W_G[i] )
            print('\n Languages \n')
            print(West['b. Languages'])
            print('\n Religion \n')
            print(West['c. Religions'])
            print('\n Clothes \n')
            print(West['d. Clothes'])
            print('\n Food \n')
            print(West['e. Food'])
            print('\n Festival \n')
            print(West['f. Festivals'])
            print('\n Heritage Sites\n')
            for i in W_hs.keys():
                print(i+"-: ", W_hs[i] )
            print('\n Literature \n')
            print(West['h. Literature'])
            print('\n Music \n')
            print(West['i. Music'])
            print('\n Dance \n')   
            print(West['j. Dance'])
        else:
            print('\n Please input the correct command ')
    

#east
    elif ans=='d':
        for key in East.keys():
            sleep(0.5)
            print(key, end='\n')
        sleep(0.5)
        #choice of aspect
        answ= input('Which aspect do you want to learn about this region: ').lower()
        for i in answ.split(' '):
            if i == 'geography':
                ans='a'
            elif i == 'language' or i =='languages':
                ans='b'
            elif i == 'religion' or i =='religions':
                ans='c'
            elif i == 'clothes':
                ans='d'
            elif i == 'food' or i=='eat':
                ans='e'
            elif i == 'heritage' or i=='monuments':
                ans='g'
            elif i == 'festivals':
                ans='f'
            elif i == 'music':
                ans='i'
            elif i == 'literature':
                ans='h'
            elif i == 'dance':
                ans='j'
            elif i == 'everything' or i == 'all':
                ans='k'
        if ans == 'a':
            sleep(0.5)
            #geographics
            print(East['a. Geography'])
        elif ans == 'b':
             #languages
            sleep(0.5)
            print(East['b. Languages'])
        elif ans == 'c':
            #religions
            sleep(0.5)
            print(East['c. Religions'])
        elif ans == 'd':
            #clothes
            sleep(0.5)
            print(East['d. Clothes'])
        elif ans == 'e':
            #food
            sleep(0.5)
            print(East['e. Food'])
        elif ans == 'f':
            #festivals
            sleep(0.5)
            for i in E_festivals.keys():
                print(i+"-: ", E_festivals[i])
        elif ans == 'g':
            #Heritage sites
            sleep(0.5)
            for i in E_hs.keys():
                print(i+"-: ", E_hs[i] )
        elif ans == 'h':
            #literature/craft
            sleep(0.5)
            print(East['h. Dance'])
        elif ans == 'i':
            #music
            sleep(0.5)
            print(East['i. Music'])
        elif ans == 'j':
            #Dance
            sleep(0.5)
            print(East['j. Literature'])
        elif ans == 'k':
             #all
            sleep(0.5)
            print('\n Geography \n')
            print(East['a. Geography'])
            print('\n Languages \n')
            print(East['b. Languages'])
            print('\n Religion \n')
            print(East['c. Religions'])
            print('\n Clothes \n')
            print(East['d. Clothes'])
            print('\n Food \n')
            print(East['e. Food'])
            print('\n Festival \n')
            for i in E_festivals.keys():
                print(i+"-: ", E_festivals[i] )
            print('\n Heritage Sites\n')
            for i in E_hs.keys():
                print(i+"-: ", E_hs[i] )
            print('\n Dance \n')
            print(East['h. Dance'])
            print('\n Music \n')
            print(East['i. Music'])
            print('\n Literature \n')
            print(East['j. Literature'])
        else:
            print('\n Please input the correct command ')
    

    elif ans=='e':
        for key in North_east.keys():
            sleep(0.5)
            print(key, end='\n')
        sleep(0.5)
        #choice of aspect
        answ= input('Which aspect do you want to learn about this region: ').lower()
        for i in answ.split(' '):
            if i == 'geography':
                ans='a'
            elif i == 'language' or i =='languages':
                ans='b'
            elif i == 'religion' or i =='religions':
                ans='c'
            elif i == 'clothes':
                ans='d'
            elif i == 'food' or i=='eat':
                ans='e'
            elif i == 'heritage' or i=='monuments':
                ans='g'
            elif i == 'festivals':
                ans='f'
            elif i == 'music':
                ans='i'
            elif i == 'literature':
                ans='h'
            elif i == 'dance':
                ans='j'
            elif i == 'everything' or i == 'all':
                ans='k'
        if ans == 'a':
            #geographics
            sleep(0.5)
            for i in NE_G.keys():
                print(i+"-: ", NE_G[i] )
        elif ans == 'b':
             #languages
            sleep(0.5)
            print(North_east['b. Languages'])
        elif ans == 'c':
            #religions
            sleep(0.5)
            print(North_east['c. Religions'])
        elif ans == 'd':
            #clothes
            sleep(0.5)
            print(North_east['d. Clothes'])
        elif ans == 'e':
            #food
            sleep(0.5)
            print(North_east['e. Food'])
        elif ans == 'f':
            #festivals
            sleep(0.5)
            for i in NE_festivals.keys():
                print(i+"-: ", NE_festivals[i])
        elif ans == 'g':
            #Heritage sites
            sleep(0.5)
            print(North_east['g. Heritage sites'])
        elif ans == 'h':
            #literature/craft
            sleep(0.5)
            print(North_east['h. Dance'])
        elif ans == 'i':
            #music
            sleep(0.5)
            print(North_east['i. Music'])
        elif ans == 'j':
            #Dance
            sleep(0.5)
            print(North_east['j. Literature'])
        elif ans == 'k':
             #all
            print('\n Geography \n')
            for i in NE_G.keys():
                print(i+"-: ", NE_G[i] )
            print('\n Languages \n')
            print(North_east['b. Languages'])
            print('\n Religion \n')
            print(North_east['c. Religions'])
            print('\n Clothes \n')
            print(North_east['d. Clothes'])
            print('\n Food \n')
            print(North_east['e. Food'])
            print('\n Festival \n')
            for i in NE_festivals.keys():
                print(i+"-: ", NE_festivals[i] )
            print('\n Heritage Sites\n')
            print(North_east['g. Heritage sites'])
            print('\n Dance \n')
            print(North_east['h. Dance'])
            print('\n Music \n')
            print(North_east['i. Music'])
            print('\n Literature \n')
            print(North_east['j. Literature'])
            sleep(0.5)
        else:
            print('\n Please input the correct command ')
    else:
        print('\n Please input the correct command ')
 

    #introduction
print('Hello, My name is Lakshmi- The chatbot')
speech = gTTS('Hello, My name is Lakshmi- The chatbot' )
speech.save('greetings1.mp3')
playsound('greetings1.mp3')
sleep(0.5)
ans= input('What is your name')
s = gTTS('What is your Name:' )
s.save('greetings2.mp3')
playsound('greetings2.mp3')
sleep(0.5)
print(' Hello '+ans+", I am here to sail you through the culture of india. What would you like to learn about the Indian culture today? ")
s = gTTS(' Hello '+ans+", I am here to sail you through the culture of india. What would you like to learn about the Indian culture today? ")
s.save('greetings3.mp3')
playsound('greetings3.mp3')
sleep(0.5)
Main()
while True:
    Q = input('\n To learn more about India please type r and to exit the code please type e: ').lower()
    s = gTTS( 'To learn more about India please type r and to exit the code please type e: ')
    s.save('reset.mp3')
    playsound('reset.mp3')
    if Q == 'r':
        Main()
    elif Q =='e':
        end_salutations= choice(End_salutations)
        print(end_salutations)
        s = gTTS( end_salutations)
        s.save('endSalutation.mp3')
        playsound('endSalutation.mp3')
        break
    else:
        print('\n Please input the correct command ')
        s = gTTS('Please input the correct command')
        s.save('correct_command.mp3')
        playsound('correct_command.mp3')

