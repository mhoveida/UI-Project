# Maddison Hoveida UNI: mh4572

from flask import Flask, render_template, request, redirect, url_for, jsonify
import datetime

app = Flask(__name__)

bungalows = {
     "1": {
        "id": "1",
        "title": "Four Seasons Bora Bora",
        "image": "https://lh3.googleusercontent.com/p/AF1QipOK175PnVM58lYJuFxuL94jMEVX3WF6NdkWU8Xs=s1360-w1360-h1020",
        "year": "2008",
        "summary": "The Four Seasons Bora Bora offers luxurious overwater bungalows with breathtaking views of Mount Otemanu. Each bungalow features traditional Polynesian decor, a private plunge pool, and direct access to the turquoise lagoon. Guests can enjoy world-class dining, a holistic spa, and a variety of water sports. The resort emphasizes sustainability and cultural immersion, offering authentic experiences like traditional dance performances and local cuisine.",
        "price_per_night": "$1,800",
        "location": "Bora Bora, French Polynesia",
        "amenities": ["Private plunge pool", "Direct lagoon access", "Spa", "Multiple restaurants", "Fitness center"],
        "rating": "4.8",
        "similar_bungalow_ids": ["2", "3", "9"],
        "activities": ["Snorkeling", "Jet skiing", "Sunset cruises", "Cultural tours"],
        "best_season": ["May", "June", "September", "October"],
        "reviews": [
            {
                "reviewer_name": "Sarah Thompson",
                "rating": "4.9",
                "date": "March 2024",
                "text": "The overwater bungalow experience was absolutely magical. Waking up to the sound of gentle waves and being able to snorkel right from our deck made this stay unforgettable."
            },
            {
                "reviewer_name": "Michael Chen",
                "rating": "4.7",
                "date": "February 2024",
                "text": "Service was impeccable and the views were stunning. The only minor issue was intermittent WiFi, but who needs internet when paradise is right outside your window?"
            }
        ]
    },
    "2": {
        "id": "2",
        "title": "Mercure Maldives Kooddoo Resort",
        "image": "https://lh3.googleusercontent.com/p/AF1QipMYd0bVc2p8FjCYaxgFr8a0ZRJRJEnkleV7Lbh5=s1360-w1360-h1020",
        "year": "2017",
        "summary": "Mercure Maldives Kooddoo Resort offers the unique advantage of being the only resort in the Maldives with a domestic airport on the island, eliminating the need for speedboat or seaplane transfers. The overwater villas feature private terraces with stairs leading directly into the crystal-clear lagoon. Each villa is designed with contemporary aesthetics while incorporating local Maldivian elements throughout the décor. The resort is situated near one of the best diving spots in the Gaafu Alifu Atoll, home to vibrant coral gardens and diverse marine life.",
        "price_per_night": "$550",
        "location": "Kooddoo Island, Maldives",
        "amenities": ["Direct lagoon access", "Private sundeck", "Rain shower", "Beach club access", "Complimentary water sports"],
        "rating": "4.6",
        "similar_bungalow_ids": ["1", "5", "9"],
        "activities": ["Diving", "Paddleboarding", "Fishing excursions", "Island hopping"],
        "best_season": ["November", "December", "January", "February", "March"],
        "reviews": [
            {
                "reviewer_name": "Alex Rodriguez",
                "rating": "4.8",
                "date": "January 2024",
                "text": "The direct access to the lagoon was amazing. We spent hours snorkeling and saw so many different fish species right from our villa."
            },
            {
                "reviewer_name": "Emma Williams",
                "rating": "4.5",
                "date": "December 2023",
                "text": "The convenience of having the domestic airport on the island made our arrival so smooth. No long boat transfers after a long flight was a huge plus."
            }
        ]
    },
    "3": {
        "id": "3",
        "title": "Pullman Maldives Maamutaa",
        "image": "https://lh3.googleusercontent.com/p/AF1QipP3kOgDkN7TqClir3-C-hfi3Yl_yYvVEYjDKhz7=s1360-w1360-h1020",
        "year": "2019",
        "summary": "Pullman Maldives Maamutaa is home to the world's first underwater bungalows with submerged bedrooms offering panoramic views of marine life. The resort operates on an all-inclusive concept that includes a wide range of culinary experiences across its six restaurants and bars. Each overwater villa features a private infinity pool and an outdoor shower with uninterrupted views of the Indian Ocean. The resort's house reef is known for its abundance of manta rays, turtles, and over 1,200 species of tropical fish.",
        "price_per_night": "$1,200",
        "location": "Gaafu Alifu Atoll, Maldives",
        "amenities": ["Underwater bedroom", "Private infinity pool", "All-inclusive dining", "Fitness center", "Spa access"],
        "rating": "4.8",
        "similar_bungalow_ids": ["1", "14", "13"],
        "activities": ["Manta ray watching", "Turtle safaris", "Cooking classes", "Yoga sessions"],
        "best_season": ["December", "January", "February", "March", "April"],
        "reviews": [
            {
                "reviewer_name": "David Johnson",
                "rating": "5.0",
                "date": "March 2024",
                "text": "The underwater bedroom was a once-in-a-lifetime experience. Falling asleep watching reef sharks and colorful fish swim by was surreal."
            },
            {
                "reviewer_name": "Sophia Garcia",
                "rating": "4.7",
                "date": "January 2024",
                "text": "The all-inclusive dining options were fantastic with six different restaurants to choose from. The infinity pool overlooking the ocean was the perfect spot for sunset cocktails."
            }
        ]
    },
    "4": {
        "id": "4",
        "title": "Hard Rock Hotel Maldives",
        "image": "https://lh3.googleusercontent.com/proxy/s1LTA9pp-0JBSPZzvs-CtmEQ_CZEmy1msJEDm7nSOvBo6NdI0x0351T1hmGB4nZ81wgYM1FiKY-lMqF4LqI7l-9BOi1r0byIj7YouSPK-e3xsxibI8WrxMHnxj9xkbOfUfctxV7R5LbynAhqM0f6bC44VXF-Fg=s1360-w1360-h1020",
        "year": "2019",
        "summary": "Hard Rock Hotel Maldives brings the iconic music-themed experience to paradise with overwater villas featuring the brand's signature Rock Star service. Each villa comes equipped with a Fender guitar and amplifier as part of the Sound of Your Stay program, allowing guests to rock out in privacy. The property is connected by footbridge to The Marina at Crossroads, offering guests access to shopping, entertainment, and dining options beyond the resort. The overwater spa pavilions feature glass floors, allowing guests to observe marine life during their treatments.",
        "price_per_night": "$700",
        "location": "South Malé Atoll, Maldives",
        "amenities": ["In-room instruments", "Music streaming service", "Rock Spa", "Recording studio access", "Roxity Kids Club"],
        "rating": "4.7",
        "similar_bungalow_ids": ["5", "15", "22"],
        "activities": ["Live music performances", "DJ lessons", "Marine conservation", "Water sports"],
        "best_season": ["January", "February", "March", "April", "December"],
        "reviews": [
            {
                "reviewer_name": "Jack Wilson",
                "rating": "4.8",
                "date": "February 2024",
                "text": "The Fender guitar in our villa was an awesome touch! As a musician, being able to play while overlooking the ocean was an incredible experience."
            },
            {
                "reviewer_name": "Lisa Brown",
                "rating": "4.6",
                "date": "December 2023",
                "text": "The Rock Spa was incredible - getting a massage while watching fish swim beneath you is something I'll never forget. The music theme throughout was fun without being overwhelming."
            }
        ]
    },
    "5": {
        "id": "5",
        "title": "Lily Beach Resort & Spa",
        "image": "https://lh3.googleusercontent.com/p/AF1QipMk3xuu8NZG85CpBM71N-kr8XHon8n43twgyoMj=s1360-w1360-h1020",
        "year": "2009",
        "summary": "Lily Beach Resort & Spa pioneered the premium all-inclusive concept in the Maldives with its Platinum Plan. The resort's lagoon villas are perched over one of the most vibrant house reefs in the Maldives, home to reef sharks, rays, and colorful coral formations. Each villa features traditional Maldivian architecture with thatched roofs and modern amenities including outdoor jacuzzis. The resort's strategic location in the South Ari Atoll puts it near several renowned whale shark spotting points, offering guests unique marine encounters.",
        "price_per_night": "$850",
        "location": "South Ari Atoll, Maldives",
        "amenities": ["Platinum all-inclusive", "Outdoor jacuzzi", "Sunset deck", "Premium drinks", "PADI dive center"],
        "rating": "4.9",
        "similar_bungalow_ids": ["1", "7", "11"],
        "activities": ["Whale shark expeditions", "Night fishing", "Sunset cruises", "Beach volleyball"],
        "best_season": ["November", "December", "January", "February", "March"],
        "reviews": [
            {
                "reviewer_name": "Thomas Wilson",
                "rating": "4.9",
                "date": "March 2024",
                "text": "The Platinum all-inclusive plan was worth every penny. Premium drinks, excellent dining options, and activities all included made for a stress-free vacation."
            },
            {
                "reviewer_name": "Olivia Martinez",
                "rating": "5.0",
                "date": "January 2024",
                "text": "We went on the whale shark expedition and actually spotted two! The house reef was incredible too - we saw sharks, rays, and countless fish species just steps from our villa."
            }
        ]
    },
    "6": {
        "id": "6",
        "title": "Kuredhivaru Resort & Spa Maldives",
        "image": "https://lh3.googleusercontent.com/p/AF1QipM4Fl8bvsN6PXvmyslhFZ2NZzL6vaVIDbMRSoHa=s1360-w1360-h1020",
        "year": "2018",
        "summary": "Kuredhivaru Resort & Spa sits in the Noonu Atoll, known for its pristine waters and abundant marine biodiversity. The overwater villas feature a minimalist Japanese-inspired design that emphasizes natural materials and clean lines. Each villa includes a private pool that extends toward the horizon, creating a seamless blend with the ocean. The resort's conservation center conducts daily coral planting activities, allowing guests to contribute to reef restoration while learning about marine ecosystems.",
        "price_per_night": "$920",
        "location": "Noonu Atoll, Maldives",
        "amenities": ["Japanese soaking tub", "Private pool", "Yoga pavilion", "Champagne breakfasts", "Marine conservation"],
        "rating": "4.8",
        "similar_bungalow_ids": ["3", "13", "14"],
        "activities": ["Coral planting", "Dolphin watching", "Meditation", "Japanese cooking classes"],
        "best_season": ["January", "February", "March", "April", "December"],
        "reviews": [
            {
                "reviewer_name": "Kevin Parker",
                "rating": "4.7",
                "date": "February 2024",
                "text": "The Japanese-inspired design was stunning and created such a peaceful atmosphere. The private pool that blends with the ocean horizon is an architectural marvel."
            },
            {
                "reviewer_name": "Natalie Kim",
                "rating": "4.9",
                "date": "January 2024",
                "text": "Participating in the coral planting activity was a highlight of our trip. It felt good to contribute to marine conservation while enjoying such luxury."
            }
        ]
    },
    "7": {
        "id": "7",
        "title": "OBLU NATURE Helengeli by Sentido",
        "image": "https://lh3.googleusercontent.com/p/AF1QipPm17SjrNCovTxG4aZakVbdxQI-Z587Mp9W_cPa=s1360-w1360-h1020",
        "year": "2015",
        "summary": "OBLU NATURE Helengeli offers an all-inclusive experience focused on sustainable luxury and natural immersion. The channel running beside the island is famous for its strong currents that attract marine megafauna including manta rays, sharks, and turtles year-round. Each overwater villa is designed with eco-friendly materials and features solar water heating systems. The resort's unique location at the edge of a channel allows guests to experience both calm lagoon waters and adventurous diving in the same location.",
        "price_per_night": "$480",
        "location": "North Malé Atoll, Maldives",
        "amenities": ["Eco-friendly design", "All-inclusive dining", "Snorkeling equipment", "Channel access", "Overwater fitness center"],
        "rating": "4.7",
        "similar_bungalow_ids": ["5", "11", "12"],
        "activities": ["Channel diving", "Eco tours", "Marine biology presentations", "Sustainable fishing"],
        "best_season": ["January", "February", "March", "April", "May"],
        "reviews": [
            {
                "reviewer_name": "Robert Chang",
                "rating": "4.6",
                "date": "March 2024",
                "text": "The channel diving was incredible - we saw manta rays, reef sharks, and a huge variety of fish. The eco-friendly focus of the resort was evident in everything from the construction to the daily operations."
            },
            {
                "reviewer_name": "Amanda Scott",
                "rating": "4.8",
                "date": "February 2024",
                "text": "The all-inclusive package was comprehensive and the overwater fitness center provided stunning views during our morning workouts. The marine biology presentations were fascinating and educational."
            }
        ]
    },
    "8": {
        "id": "8",
        "title": "LUX South Ari Atoll",
        "image": "https://lh3.googleusercontent.com/p/AF1QipOIN0tllHCKSGdMrHXuKIeZfWJdaUwNH9HnapsS=s1360-w1360-h1020",
        "year": "2016",
        "summary": "LUX* South Ari Atoll features the world's largest overwater solar system, powering a significant portion of the resort's electricity needs. The overwater villas showcase contemporary design with panoramic glass walls that can be fully opened to transform the living space into an open-air pavilion. The resort houses eight restaurants offering diverse international cuisines ranging from Japanese to Mediterranean. LUX* is known for its surprise pop-up experiences that appear and disappear throughout the property, creating unique moments for guests.",
        "price_per_night": "$780",
        "location": "South Ari Atoll, Maldives",
        "amenities": ["Solar-powered villas", "Overwater cinema", "Secret bars", "Bicycle for each villa", "Wanderlust library"],
        "rating": "4.8",
        "similar_bungalow_ids": ["1", "10", "14"],
        "activities": ["Photography workshops", "Pop-up experiences", "Marine conservation", "Mixology classes"],
        "best_season": ["November", "December", "January", "February", "March"],
        "reviews": [
            {
                "reviewer_name": "Daniel Thompson",
                "rating": "5.0",
                "date": "March 2024",
                "text": "The pop-up experiences were such a wonderful surprise! We discovered a secret cinema on the beach one night and a cocktail bar hidden in the jungle another day."
            },
            {
                "reviewer_name": "Julia Patel",
                "rating": "4.7",
                "date": "January 2024",
                "text": "Having eight restaurant options meant we never got bored with the food. The photography workshop helped me capture the beauty of our stay professionally."
            }
        ]
    },
    "9": {
        "id": "9",
        "title": "SO/ Maldives",
        "image": "https://lh3.googleusercontent.com/proxy/U2WZ2VR7etE9BMUCS04AypK4BsySJv1ISoh-zKTdTRxDCQvP_W9Gi8R5FwbDSF5yDPOuAcsbi--tIg3chwR0JQPjgBp1aL1uCPwrrP_mJEOnvAbIlP6ejUQ6IetWbkn7NgbZyZ6FXgbqjJhkf1Nhbudr-Ts1bw=s680-w680-h510", 
        "year": "2023",
        "summary": "SO/ Maldives represents the newest generation of overwater luxury with its avant-garde design and fashion-forward concept. Each villa features artwork and elements designed by renowned fashion designers, creating unique visual experiences. The resort houses the Maldives' first overwater nightclub with international DJs in residence throughout the high season. The innovative glass-bottomed overwater spa combines traditional treatments with chromotherapy as fish swim beneath the treatment beds.",
        "price_per_night": "$1,100",
        "location": "Emboodhoo Lagoon, Maldives",
        "amenities": ["Designer interiors", "Overwater nightclub", "Fashion library", "Glass-bottomed spa", "Personal mixologist"],
        "rating": "4.7",
        "similar_bungalow_ids": ["4", "15", "22"],
        "activities": ["Fashion shows", "DJ sessions", "Cocktail masterclasses", "Underwater photography"],
        "best_season": ["December", "January", "February", "March", "April"],
        "reviews": [
            {
                "reviewer_name": "Victoria Stevens",
                "rating": "4.8",
                "date": "March 2024",
                "text": "As a fashion enthusiast, I was blown away by the designer interiors and fashion library. The overwater nightclub was unlike anything I've experienced before - dancing under the stars above the ocean!"
            },
            {
                "reviewer_name": "Ryan Morris",
                "rating": "4.6",
                "date": "February 2024",
                "text": "The personal mixologist created custom cocktails based on our preferences each evening. The glass-bottomed spa was incredible - watching tropical fish swim beneath you during a massage is surreal."
            }
        ]
    },
    "10": {
        "id": "10",
        "title": "Anantara Veli Maldives Resort",
        "image": "https://lh3.googleusercontent.com/p/AF1QipNtq1pmEQdPyDBSgbOajM72EdPAXHxixD34eUcJ=s1360-w1360-h1020",
        "year": "2012",
        "summary": "Anantara Veli operates as an adults-only sanctuary, offering a tranquil experience without the presence of children. The overwater bungalows feature traditional Maldivian architecture with contemporary touches and expansive decks for private sunbathing. The resort is connected by boat to its sister property, allowing guests to access additional dining options and facilities. Anantara Veli is known for its overwater spa that incorporates traditional Thai wellness practices with local Maldivian healing techniques.",
        "price_per_night": "$620",
        "location": "South Malé Atoll, Maldives",
        "amenities": ["Adults-only", "Thai spa", "Wine cellar", "Yoga pavilion", "Inter-island access"],
        "rating": "4.8",
        "similar_bungalow_ids": ["1", "5", "11"],
        "activities": ["Couples spa rituals", "Wine tastings", "Traditional fishing", "Cooking classes"],
        "best_season": ["January", "February", "March", "April", "December"],
        "reviews": [
            {
                "reviewer_name": "James Wilson",
                "rating": "4.9",
                "date": "March 2024",
                "text": "The adults-only policy created such a peaceful atmosphere. The Thai spa treatments were some of the best we've ever experienced, and the wine tastings were exceptional."
            },
            {
                "reviewer_name": "Elizabeth Taylor",
                "rating": "4.7",
                "date": "January 2024",
                "text": "Having access to the sister property gave us so many more dining options. The traditional Maldivian fishing excursion was both educational and fun - we caught our dinner!"
            }
        ]
    },
    "11": {
        "id": "11",
        "title": "Kihaa Maldives",
        "image": "https://lh3.googleusercontent.com/proxy/sRT0D6eD6Vtxkw56FGUATbjkbJo__jU0PQjZjgHKDiD0ulylzz5CKyeOttwsLWjyuJ-myyIqifE9Io_nQqOwrH2oX73uZ58flDuOsRtuv3do9XgqQT8VV2gfAhgQOlPI_7KpStqIGFC8L3yjktz1WHTXdAufYxM=s1360-w1360-h1020",
        "year": "2012",
        "summary": "Kihaa Maldives is located in the UNESCO Biosphere Reserve of Baa Atoll, known for its exceptional marine biodiversity. The resort is just 15 minutes by boat from Hanifaru Bay, famous for its seasonal congregation of manta rays and whale sharks. Each overwater villa features traditional Maldivian architecture with high ceilings and natural ventilation systems that minimize the need for air conditioning. The resort runs on a hybrid power system combining solar energy and traditional generators to reduce its environmental footprint.",
        "price_per_night": "$490",
        "location": "Baa Atoll, Maldives",
        "amenities": ["Biosphere location", "Natural cooling", "Coral adoption", "Telescope", "Local handicrafts"],
        "rating": "4.6",
        "similar_bungalow_ids": ["5", "7", "12"],
        "activities": ["Manta ray excursions", "Marine conservation", "Local island visits", "Astronomy sessions"],
        "best_season": ["June", "July", "August", "September", "October"],
        "reviews": [
            {
                "reviewer_name": "Matthew Hansen",
                "rating": "4.7",
                "date": "September 2023",
                "text": "Swimming with manta rays in Hanifaru Bay was a bucket list experience fulfilled! The resort's commitment to conservation was evident in their coral adoption program and sustainable practices."
            },
            {
                "reviewer_name": "Sarah Johnson",
                "rating": "4.5",
                "date": "August 2023",
                "text": "The natural ventilation system was impressive and kept the villa comfortable without excessive air conditioning. The astronomy sessions under the unpolluted night sky were magical."
            }
        ]
    },
    "12": {
        "id": "12",
        "title": "Atmosphere Kanifushi",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/84/af/12/water-villa-with-pool.jpg?w=1400&h=-1&s=1",
        "year": "2013",
        "summary": "Atmosphere Kanifushi pioneered the premium all-inclusive concept in the Maldives with its Platinum Plus plan that includes premium dining and activities. The resort sits on one of the longest islands in the Maldives, featuring a two-kilometer pristine beach alongside its overwater villas. Each villa is designed with sustainability in mind, using renewable materials and energy-efficient systems throughout. The resort's location in the remote Lhaviyani Atoll offers guests exceptional privacy and access to less frequented dive sites.",
        "price_per_night": "$870",
        "location": "Lhaviyani Atoll, Maldives",
        "amenities": ["Platinum Plus inclusive", "Private island setting", "Sunset fishing", "Premium spirits", "Daily excursions"],
        "rating": "4.8",
        "similar_bungalow_ids": ["5", "7", "11"],
        "activities": ["Sunset dolphin cruise", "White-water dives", "Cultural performances", "Water sports"],
        "best_season": ["December", "January", "February", "March", "April"],
        "reviews": [
            {
                "reviewer_name": "Christopher Lee",
                "rating": "4.9",
                "date": "February 2024",
                "text": "The Platinum Plus all-inclusive was the most comprehensive we've experienced. Premium spirits, daily excursions, and gourmet dining all included - truly worry-free luxury."
            },
            {
                "reviewer_name": "Jessica Wong",
                "rating": "4.7",
                "date": "January 2024",
                "text": "The sunset dolphin cruise was magical - we saw dozens of dolphins playing in the golden light. The two-kilometer beach meant we always found a private spot to relax."
            }
        ]
    },
    "13": {
        "id": "13",
        "title": "Soneva Jani",
        "image": "https://lh3.googleusercontent.com/p/AF1QipPuQLl5i-hxcg68L3AyQsQAkFGcKWqAppoQApJM=s1360-w1360-h1020",
        "year": "2016",
        "summary": "Soneva Jani represents the pinnacle of sustainable luxury with its innovative overwater villas featuring retractable roofs for stargazing directly from bed. Each villa comes with a water slide that spirals directly from the upper deck into the lagoon. The resort operates on a 100% carbon-neutral basis, with extensive solar installations and waste-to-wealth programs. Soneva Jani's Observatory houses the largest telescope in the Indian Ocean, offering guided astronomy experiences with resident experts.",
        "price_per_night": "$2,500",
        "location": "Noonu Atoll, Maldives",
        "amenities": ["Retractable roof", "Private waterslide", "Outdoor cinema", "Astronomical observatory", "Personal butler"],
        "rating": "5.0",
        "similar_bungalow_ids": ["3", "14", "15"],
        "activities": ["Astronomy sessions", "Sustainable gardening", "Overwater cinema", "Silent disco"],
        "best_season": ["December", "January", "February", "March", "April"],
        "reviews": [
            {
                "reviewer_name": "William Peterson",
                "rating": "5.0",
                "date": "March 2024",
                "text": "The retractable roof was incredible - falling asleep under the stars and waking up to the sunrise without leaving your bed. The waterslide from our villa directly into the lagoon brought out our inner child!"
            },
            {
                "reviewer_name": "Charlotte Davis",
                "rating": "5.0",
                "date": "February 2024",
                "text": "The astronomy session with the resident expert was fascinating, and the carbon-neutral operations show luxury can be sustainable. This was truly the best hotel experience of our lives."
            }
        ]
    },
    "14": {
        "id": "14",
        "title": "Anantara Dhigu Maldives Resort",
        "image": "https://lh3.googleusercontent.com/p/AF1QipMQR1VGDe8Wq65Gvz_cghyrdqOCdEwJYEDL3F_R=s1360-w1360-h1020",
        "year": "2006",
        "summary": "Anantara Dhigu offers family-friendly overwater villas with special safety features including enclosed terraces and shallow lagoon sections. The resort is interconnected with two sister properties via boat shuttle, giving guests access to over 15 dining venues across three islands. Each sunset-facing villa features an oversized bathtub with panoramic ocean views and a dedicated swing bed suspended over the water. The resort's marine biology center conducts coral restoration projects that guests can participate in.",
        "price_per_night": "$750",
        "location": "South Malé Atoll, Maldives",
        "amenities": ["Family-friendly design", "Multi-resort access", "Sunset views", "Swing beds", "Children's club"],
        "rating": "4.7",
        "similar_bungalow_ids": ["1", "8", "10"],
        "activities": ["Family snorkeling", "Coral adoption", "Dhoni sailing", "Marine biology sessions"],
        "best_season": ["December", "January", "February", "March", "April"],
        "reviews": [
            {
                "reviewer_name": "Mark and Karen Williams",
                "rating": "4.8",
                "date": "March 2024",
                "text": "Traveling with kids can be challenging, but Anantara Dhigu made it a breeze. The safety features in the villa gave us peace of mind while the children's club kept our kids entertained."
            },
            {
                "reviewer_name": "Samantha Hughes",
                "rating": "4.6",
                "date": "January 2024",
                "text": "The swing bed over the water was our daughter's favorite feature. Having access to 15 restaurants across three islands meant we never had to worry about picky eaters getting bored with the food."
            }
        ]
    },
    "15": {
        "id": "15",
        "title": "The Standard, Huruvalhi Maldives",
        "image": "https://lh3.googleusercontent.com/p/AF1QipNpyGPoXnRUxjHUzhKauKcXFvjEfO5MQt2R-nBI=s680-w680-h510",
        "year": "2019",
        "summary": "The Standard, Huruvalhi Maldives brings the brand's vibrant urban energy to an overwater setting with a focus on social experiences and wellness. Each villa features a private plunge pool and direct lagoon access via a slide, creating a playful luxury experience. The resort hosts the only underground nightclub in the Maldives, built beneath the island and featuring international DJs. The property's innovative glass-bottomed overwater yoga pavilion allows participants to practice while observing marine life beneath their mats.",
        "price_per_night": "$650",
        "location": "Raa Atoll, Maldives",
        "amenities": ["Adult playground", "Underground club", "Hammock in water", "Floating bar", "Glass yoga studio"],
        "rating": "4.6",
        "similar_bungalow_ids": ["4", "9", "22"],
        "activities": ["Full moon parties", "BBQ beach dinners", "Underwater disco", "Inflatable water park"],
        "best_season": ["January", "February", "March", "April", "May"],
        "reviews": [
            {
                "reviewer_name": "Tyler Brooks",
                "rating": "4.7",
                "date": "March 2024",
                "text": "The vibe at The Standard is completely different from any other resort in the Maldives - it's fun, young, and energetic. The underground nightclub was amazing and the full moon party was unforgettable."
            },
            {
                "reviewer_name": "Emily Zhang",
                "rating": "4.5",
                "date": "February 2024",
                "text": "The glass yoga studio was such a unique experience - doing downward dog while watching stingrays swim beneath you is surreal. The hammock in the water was my favorite spot for afternoon naps."
            }
        ]
    },
    "16": {
        "id": "16",
        "title": "Palafitos Overwater Bungalows",
        "image": "https://lh3.googleusercontent.com/p/AF1QipNs0K89GBebQ85AVRMmEGicSoq2npmy24vKEgDz=s1360-w1360-h1020",
        "year": "2016",
        "summary": "Palafitos Overwater Bungalows was the first luxury overwater accommodation in Mexico, bringing the Maldivian concept to the Caribbean. Each bungalow features glass floor panels throughout the bedroom and living areas for continuous marine viewing. The exclusive adults-only section offers a dedicated overwater restaurant serving Yucatan-inspired cuisine with Caribbean influences. The resort's location on Mexico's Riviera Maya provides easy access to ancient Mayan ruins and the world's second-largest barrier reef system.",
        "price_per_night": "$720",
        "location": "Riviera Maya, Mexico",
        "amenities": ["Glass floors", "Ladder access", "Private infinity pool", "Outdoor shower", "Overwater restaurant"],
        "rating": "4.7",
        "similar_bungalow_ids": ["19", "20", "21"],
        "activities": ["Cenote diving", "Mayan ruins tours", "Tequila tastings", "Mexican cooking classes"],
        "best_season": ["November", "December", "January", "February", "March"],
        "reviews": [
            {
                "reviewer_name": "Richard Gonzalez",
                "rating": "4.8",
                "date": "February 2024",
                "text": "We loved that we could experience overwater luxury without traveling to the Maldives. The glass floors were amazing - we saw stingrays, fish, and even an octopus under our bungalow!"
            },
            {
                "reviewer_name": "Melissa King",
                "rating": "4.6",
                "date": "January 2024",
                "text": "The combination of overwater luxury and access to Mayan cultural sites made this a unique experience. The Yucatan-inspired cuisine at the overwater restaurant was exceptional."
            }
        ]
    },
    "17": {
        "id": "17",
        "title": "Kish Toranj Marine Hotel",
        "image": "https://lh3.googleusercontent.com/p/AF1QipPJougqCTyKi9VHkfGq1kpXy1k_BhxxVsGJ78qh=s1360-w1360-h1020",
        "year": "2016",
        "summary": "The Toranj Marine Hotel features Iran's first overwater bungalows on the picturesque Kish Island in the Persian Gulf. The distinctive circular design of each villa draws inspiration from traditional Persian architecture while incorporating modern luxury elements. Floor-to-ceiling windows showcase the turquoise waters, while private terraces offer direct sea access for swimming and snorkeling. These accommodations represent the evolving luxury tourism sector in Iran, combining cultural heritage with international hospitality standards.",
        "price_per_night": "$420",
        "location": "Iran",
        "amenities": ["Private terrace","Direct sea access","Persian spa treatments","Traditional tea service","Sunset boat tours"],
        "rating": "4.4",
        "similar_bungalow_ids": ["19", "26", "27"],
        "activities": ["Pearl diving experiences","Traditional music performances","Water sports","Island historical tours"],
        "best_season": ["October", "November", "December", "January", "February", "March"],
        "reviews": [
            {
                "reviewer_name": "Amir Hosseini",
                "rating": "4.5",
                "date": "February 2024",
                "text": "The blend of Persian architectural elements with modern luxury was impressive. The circular design provided panoramic views of the Persian Gulf from everywhere in the villa."
            },
            {
                "reviewer_name": "Leila Zaidi",
                "rating": "4.3",
                "date": "December 2023",
                "text": "The traditional tea service on our private terrace while watching the sunset was a highlight. The Persian spa treatments incorporated local herbs and techniques I'd never experienced before."
            }
        ]
    },
    "18": {
        "id": "18",
        "title": "Sandals Grande St Lucian",
        "image": "https://lh3.googleusercontent.com/proxy/BV-gePCnXQAdmpQlUq2tridtAkY1ecyATV7rJRs6RpRfQ7NJvdJpeuGEmSU4PTqVrqOSAcRagESLeGKlF6WQzBq804yT7Vksgr_jmzSvZnkrbJOY_0ZnNEEtgJ1czrlN08tHn3wi-0BhtLo4DlfgmdjApmrTmQ=s1360-w1360-h1020",
        "year": "2017",
        "summary": "Sandals Grande St Lucian introduced the first overwater bungalows in the Eastern Caribbean, set against the backdrop of St Lucia's volcanic mountains. Each bungalow features glass floor panels, a tranquility soaking tub for two, and an overwater hammock. The resort operates on an all-inclusive concept that includes unlimited premium spirits and dining at 12 restaurants. The overwater wedding pavilion has become a signature venue for Caribbean destination weddings.",
        "price_per_night": "$1,100",
        "location": "Gros Islet, St. Lucia",
        "amenities": ["Butler service", "Overwater hammock", "Over-water wedding chapel", "Tranquility soaking tub", "All-inclusive premium spirits"],
        "rating": "4.7",
        "similar_bungalow_ids": ["21", "22", "25"],
        "activities": ["Overwater weddings", "Island hopping", "Volcano tours", "Chocolate making"],
        "best_season": ["December", "January", "February", "March", "April"],
        "reviews": [
            {
                "reviewer_name": "Jennifer and David Collins",
                "rating": "4.8",
                "date": "March 2024",
                "text": "We had our wedding at the overwater pavilion and stayed in the bungalow for our honeymoon. The entire experience was magical with the volcanic mountains as a backdrop."
            },
            {
                "reviewer_name": "Michael Stone",
                "rating": "4.6",
                "date": "February 2024",
                "text": "The butler service was exceptional - anticipating our needs before we even knew we had them. The tranquility soaking tub with panoramic views was perfect for relaxing after a day of island adventures."
            }
        ]
    },
    "19": {
        "id": "19",
        "title": "Sandals Royal Caribbean",
        "image": "https://lh3.googleusercontent.com/p/AF1QipOwRWVtQ8zWRN6zRVofiM9lG-DvFsZjean8yps9=s1360-w1360-h1020",
        "year": "2016",
        "summary": "Sandals Royal Caribbean features Jamaica's first overwater bungalows built in a heart formation when viewed from above. Each bungalow comes with dedicated butler service and 24-hour room service exclusive to overwater guests. The resort is located on its own private island, accessible by boat shuttle running throughout the day and evening. The innovative design includes glass floor panels with underwater lighting for nighttime marine viewing.",
        "price_per_night": "$1,050",
        "location": "Montego Bay, Jamaica",
        "amenities": ["Butler service", "Heart-shaped layout", "Private island", "Underwater lighting", "Extended overwater decks"],
        "rating": "4.6",
        "similar_bungalow_ids": ["20", "22", "23"],
        "activities": ["Private island dining", "Reggae beach parties", "Catamaran cruises", "Rum tastings"],
        "best_season": ["December", "January", "February", "March", "April"],
        "reviews": [
            {
                "reviewer_name": "Robert Johnson",
                "rating": "4.7",
                "date": "February 2024",
                "text": "The heart-shaped layout of the bungalows is even more beautiful when seen during our helicopter arrival. At night, the underwater lighting created a mesmerizing show of marine life beneath our villa."
            },
            {
                "reviewer_name": "Tiffany Edwards",
                "rating": "4.5",
                "date": "January 2024",
                "text": "Having our own dedicated butler made this the most luxurious stay we've ever experienced. The private island location meant peaceful seclusion but with easy access to all resort amenities."
            }
        ]
    },
    "20": {
        "id": "20",
        "title": "Royalton Antigua",
        "image": "https://lh3.googleusercontent.com/p/AF1QipMEKLEAwHQ_qeFBO33ClZJaY5SyxuBivT-mpZA7=s1360-w1360-h1020",
        "year": "2019",
        "summary": "Royalton Antigua's Chairman Overwater Bungalows represent the first and only overwater accommodations on the island. Each bungalow features a private infinity plunge pool, glass floor sections, and an overwater hammock. The resort operates on a luxury all-inclusive concept with a dedicated restaurant exclusively for overwater bungalow guests. The property's location in Deep Bay provides protected waters and sunset views framed by historic Fort Barrington.",
        "price_per_night": "$850",
        "location": "Five Islands Village, Antigua",
        "amenities": ["Infinity plunge pool", "Apple iPad room controls", "Exclusive beach area", "Dedicated restaurant", "Overwater hammock"],
        "rating": "4.5",
        "similar_bungalow_ids": ["19", "21", "2"],
        "activities": ["Historic fort tours", "Sunset sailing", "Antigua island tours", "Caribbean cooking classes"],
        "best_season": ["December", "January", "February", "March", "April"],
        "reviews": [
            {
                "reviewer_name": "Gregory Thompson",
                "rating": "4.6",
                "date": "March 2024",
                "text": "The infinity plunge pool that blends with the ocean horizon was spectacular. Having a dedicated restaurant just for overwater bungalow guests meant exceptional service and no wait times."
            },
            {
                "reviewer_name": "Alicia Rodriguez",
                "rating": "4.4",
                "date": "January 2024",
                "text": "The iPad room controls were a cool high-tech touch that made everything from lighting to ordering room service seamless. The glass floor sections provided hours of entertainment watching marine life."
            }
        ]
    },
    "21": {
        "id": "21",
        "title": "St. George's Caye Resort",
        "image": "https://lh3.googleusercontent.com/p/AF1QipOcfHAMRptNi0iKrHhPJL0W8BtDqhQt7QEoQ7Dh=s1360-w1360-h1020",
        "year": "2010",
        "summary": "St. George's Caye Resort offers rustic-luxe overwater cabanas on a private island with a rich pirate history dating back to the 1700s. Each thatch-roofed cabana features traditional Belizean hardwoods and handcrafted furniture made by local artisans. The resort sits directly on the Belize Barrier Reef, the second largest coral reef system in the world. The property operates on a nearly all-inclusive concept with a focus on marine adventures and cultural immersion.",
        "price_per_night": "$450",
        "location": "St. George's Caye, Belize",
        "amenities": ["Historical setting", "Reef location", "Local craftsmanship", "Hammocks", "Rainwater collection"],
        "rating": "4.4",
        "similar_bungalow_ids": ["24", "29", "7"],
        "activities": ["Barrier reef diving", "Manatee watching", "Fishing", "Island history tours"],
        "best_season": ["February", "March", "April", "May", "June"],
        "reviews": [
            {
                "reviewer_name": "Benjamin Clark",
                "rating": "4.5",
                "date": "April 2024",
                "text": "The rustic-luxe vibe perfectly matched the pirate history of the island. The handcrafted furniture and traditional hardwoods created an authentic Belizean experience unlike chain resorts."
            },
            {
                "reviewer_name": "Rachel Foster",
                "rating": "4.3",
                "date": "March 2024",
                "text": "Being right on the Belize Barrier Reef meant world-class diving and snorkeling just steps from our cabana. Watching manatees swim by while having breakfast on our private deck was unforgettable."
            }
        ]
    },
    "22": {
        "id": "22",
        "title": "Thatch Caye Resort",
        "image": "https://lh3.googleusercontent.com/p/AF1QipMslpWG_Bj5nRw4B6aJKOjJE3NfFSS2qF47aS6N=s680-w680-h510",
        "year": "2012",
        "summary": "Thatch Caye Resort is an eco-friendly private island featuring just 15 accommodations, including authentically designed overwater bungalows. The property operates on a sustainable model with solar power, composting, and rainwater collection systems. Each bungalow is built using locally sourced materials including thatch, bamboo, and reclaimed hardwoods. The resort's location near the Belize Barrier Reef provides exceptional snorkeling directly from the overwater accommodations.",
        "price_per_night": "$390",
        "location": "Dangriga, Belize",
        "amenities": ["Eco-friendly design", "Communal dining", "Yoga deck", "Hammock lounge", "Solar power"],
        "rating": "4.5",
        "similar_bungalow_ids": ["23", "29", "5"],
        "activities": ["Fly fishing", "Snorkeling trips", "Garifuna drumming", "Coconut husking"],
        "best_season": ["January", "February", "March", "April", "May"],
        "reviews": [
            {
                "reviewer_name": "Caroline Mitchell",
                "rating": "4.6",
                "date": "March 2024",
                "text": "The eco-friendly approach was impressive - solar power, composting, and rainwater collection systems all working seamlessly to provide luxury with minimal environmental impact."
            },
            {
                "reviewer_name": "Jason Ramirez",
                "rating": "4.4",
                "date": "February 2024",
                "text": "Communal dining was a highlight - meeting other travelers and sharing stories over fresh-caught seafood. The Garifuna drumming lessons were a unique cultural experience we'll always remember."
            }
        ]
    },
    "23": {
        "id": "23",
        "title": "Azul Paradise",
        "image": "https://lh3.googleusercontent.com/p/AF1QipMkyMY4b4ItoITahRC4ZhAsNMeMOoYfAtBVLh0W=s1360-w1360-h1020",
        "year": "2015",
        "summary": "Nestled in the pristine Bocas del Toro archipelago, Azul Paradise offers authentic overwater bungalows in one of Panama's most unspoiled regions. The eco-friendly accommodations blend seamlessly with the natural environment while providing modern comforts including solar power and sustainable water systems. Each bungalow features a private deck with direct access to the crystal-clear Caribbean waters teeming with colorful marine life. The resort's commitment to conservation includes protection of the surrounding coral reefs and mangrove ecosystems.",
        "price_per_night": "$450",
        "location": "Panama",
        "amenities": ["Hammocks","Direct ocean access","Sustainable design","Organic toiletries","Reef-friendly sunscreen provided"],
        "rating": "4.5",
        "similar_bungalow_ids": ["2", "29", "26"],
        "activities": ["Mangrove tours","Dolphin watching","Chocolate farm tours","Kayaking"],
        "best_season": ["January", "February", "March", "September", "October"],
        "reviews": [
            {
                "reviewer_name": "Isabel Murray",
                "rating": "4.6",
                "date": "March 2024",
                "text": "Bocas del Toro is a hidden gem, and Azul Paradise captures its essence perfectly. The bungalows blend with nature while providing all necessary comforts, and the mangrove tour was incredibly informative."
            },
            {
                "reviewer_name": "Anthony Lopez",
                "rating": "4.4",
                "date": "January 2024",
                "text": "We appreciated the thoughtful details like reef-friendly sunscreen and organic toiletries. The chocolate farm tour was fascinating - we learned about the entire process from bean to bar."
            }
        ]
    },
    "24": {
        "id": "24",
        "title": "Sandals South Coast",
        "image": "https://lh3.googleusercontent.com/p/AF1QipNY8HGhVeGPHp8vfvb4qp3qep0E46_LVfIXgF9P=s1360-w1360-h1020",
        "year": "2017",
        "summary": "The Over-the-Water Bungalows at Sandals South Coast create Jamaica's first overwater bungalow experience within a heart-shaped arrangement. Each bungalow features a private infinity pool, outdoor shower, and a suspended patio with Tranquility Soaking Tub for two. The glass floor panels showcase the vibrant marine ecosystem below, while hardwood floors and vaulted ceilings complement the luxury interiors. Dedicated butler service, in-room dining, and airport transfers are all included in this all-inclusive experience.",
        "price_per_night": "$1,150",
        "location": "Jamaica",
        "amenities": ["Private infinity pool","Overwater hammock","Glass floor panels","Tranquility Soaking Tub","Butler service"],
        "rating": "4.8",
        "similar_bungalow_ids": ["22", "26", "1"],
        "activities": ["Scuba diving","Water skiing","Beach volleyball","Reggae nights"],
        "best_season": ["December", "January", "February", "March", "April"],
        "reviews": [
            {
                "reviewer_name": "Derek and Olivia Wallace",
                "rating": "4.9",
                "date": "February 2024",
                "text": "The heart-shaped arrangement of bungalows is even more romantic in person than in photos. Our butler John anticipated every need and made our anniversary celebration absolutely perfect."
            },
            {
                "reviewer_name": "Stephanie Reed",
                "rating": "4.7",
                "date": "January 2024",
                "text": "The Tranquility Soaking Tub on our suspended patio was the perfect spot for evening relaxation with champagne. All-inclusive really means ALL-inclusive here - no hidden charges for premium experiences."
            }
        ]
    },
    "25": {
        "id": "25",
        "title": "Stella Island Luxury Resort & Spa",
        "image": "https://lh3.googleusercontent.com/p/AF1QipNjkrbQg6_1fbgqg5B2j1o6DDSbFtnLeRVOh296=s1360-w1360-h1020",
        "year": "2017",
        "summary": "Stella Island Luxury Resort & Spa brings the Maldivian overwater experience to the Mediterranean with stylish bungalows positioned above a lagoon-style pool. These adults-only accommodations feature private terraces with direct pool access, outdoor daybeds, and elegant interiors with natural materials and muted tones. Each bungalow includes premium amenities such as a Nespresso machine, pillow menu, and luxury bath products. The resort's design creates intimate spaces despite being part of a larger property, with careful placement ensuring privacy for each accommodation.",
        "price_per_night": "$550",
        "location": "Crete, Greece",
        "amenities": ["Private pool access","Outdoor daybed","Premium bath products","Pillow menu","Evening turndown service"],
        "rating": "4.8",
        "similar_bungalow_ids": ["13", "29", "22"],
        "activities": ["Spa treatments","Wine tasting","Yoga sessions","Greek cooking classes"],
        "best_season": ["May", "June", "July", "August", "September", "October"],
        "reviews": [
            {
                "reviewer_name": "Nicholas Anderson",
                "rating": "4.9",
                "date": "September 2023",
                "text": "Stella Island brings the Maldives to the Mediterranean! The overwater bungalows surrounding the massive lagoon pool create a tropical paradise in Greece with the added benefit of incredible local cuisine."
            },
            {
                "reviewer_name": "Sofia Papadopoulos",
                "rating": "4.7",
                "date": "August 2023",
                "text": "The adults-only policy creates a perfectly peaceful atmosphere. The pillow menu and premium amenities show attention to detail, and the Greek cooking class was a highlight of our stay."
            }
        ]
    },
    "26": {
        "id": "26",
        "title": "Villaggio La Pescaccia",
        "image": "https://lh3.googleusercontent.com/p/AF1QipNsxuwQNxGliR3jSJrAGQUT54-fjt-w5AYNy5du=s1360-w1360-h1020",
        "year": "2016",
        "summary": "Villaggio La Pescaccia offers charming floating bungalows on the serene waters of Lake Trasimeno in central Italy. Each houseboat combines rustic Italian design with modern amenities and features a private terrace perfect for watching sunsets over the lake. The interiors showcase local craftsmanship with handmade furniture and textiles from Umbrian artisans. These solar-powered accommodations represent sustainable tourism efforts in the protected lake region, with each unit constructed using eco-friendly materials and designed to minimize environmental impact.",
        "price_per_night": "$280",
        "location": "Italy",
        "amenities": ["Lake views","Private terrace","Solar power","Fishing equipment","Kayak included"],
        "rating": "4.5",
        "similar_bungalow_ids": ["22", "19", "15"],
        "activities": ["Fishing","Bird watching","Island visits","Umbrian wine tours"],
        "best_season": ["April", "May", "June", "September", "October"],
        "reviews": [
            {
                "reviewer_name": "Marco Rossi",
                "rating": "4.6",
                "date": "May 2023",
                "text": "These floating bungalows capture the essence of Italian lakeside living. The craftsmanship in the furniture and textiles showcases Umbrian artisanal traditions, and having a kayak included was perfect for morning excursions."
            },
            {
                "reviewer_name": "Claire Dubois",
                "rating": "4.4",
                "date": "September 2023",
                "text": "The sustainable approach with solar power and eco-friendly materials aligns perfectly with the natural beauty of Lake Trasimeno. Bird watching from our private terrace was a peaceful daily ritual."
            }
        ]
    },
    "27": {
        "id": "27",
        "title": "Floating Village Brombachsee",
        "image": "https://lh3.googleusercontent.com/p/AF1QipOKBHaUGPMx3HNuZ6f9K9SzkklqXIPfQUJVDRii=s1360-w1360-h1020",
        "year": "2018",
        "summary": "The Floating Village Brombachsee features modern floating homes on Bavaria's largest reservoir system. These architecturally distinct bungalows combine minimalist Scandinavian design with German engineering excellence, resulting in spacious interiors flooded with natural light. Each unit includes a rooftop terrace offering 360-degree views of the lake and surrounding nature reserve. The homes utilize innovative sustainable systems including rainwater collection and advanced insulation to minimize energy consumption throughout the seasons.",
        "price_per_night": "$340",
        "location": "Germany",
        "amenities": ["Rooftop terrace","Floor-to-ceiling windows","Boat dock","Smart home technology","Electric boat included"],
        "rating": "4.6",
        "similar_bungalow_ids": ["29", "25", "3"],
        "activities": ["Sailing","Swimming","Electric boating","Cycling along lake paths"],
        "best_season": ["May", "June", "July", "August", "September"],
        "reviews": [
            {
                "reviewer_name": "Thomas Müller",
                "rating": "4.7",
                "date": "July 2023",
                "text": "German engineering at its finest! The smart home technology made controlling everything from temperature to music seamless, and the included electric boat was perfect for exploring the reservoir."
            },
            {
                "reviewer_name": "Anna Schmidt",
                "rating": "4.5",
                "date": "August 2023",
                "text": "The minimalist Scandinavian design created a calming atmosphere, and the rooftop terrace offered spectacular sunset views. The cycling paths around the lake provided a great way to explore the nature reserve."
            }
        ]
    },
    "28": {
        "id": "28",
        "title": "Reefsuites, Whitsundays",
        "image": "https://assets.discover-the-world.com/tr:w-1440,h-960,min_width-1200,f-webp/production/app/uploads/2024/09/reefsleep-view-from-bedroom-cruise-whitsundays.jpg",
        "year": "2019",
        "summary": "Reefsuites offers Australia's first underwater accommodation experience on the Great Barrier Reef. These exclusive suites feature floor-to-ceiling windows that look directly into the heart of Hardy Reef, offering unparalleled views of marine life in their natural habitat. The premium accommodations are part of a sustainable tourism initiative that includes active reef conservation and research projects. Guests can participate in citizen science activities and educational programs about reef ecosystems during their stay.",
        "price_per_night": "$850",
        "location": "Australia",
        "amenities": ["Underwater views","All-inclusive meals","Guided snorkeling tours","Marine biologist talks","Sunset deck access"],
        "rating": "4.9",
        "similar_bungalow_ids": ["1", "13", "29"],
        "activities": ["Snorkeling","Diving","Semi-submarine tours","Helicopter flights"],
        "best_season": ["June", "July", "August", "September", "October"],
        "reviews": [
            {
                "reviewer_name": "Rebecca Watson",
                "rating": "5.0",
                "date": "September 2023",
                "text": "Falling asleep while watching fish, rays, and even reef sharks swim by our underwater window was a surreal experience. The marine biologist talks added educational value to an already incredible stay."
            },
            {
                "reviewer_name": "James Cooper",
                "rating": "4.8",
                "date": "August 2023",
                "text": "We participated in a coral planting citizen science project that made us feel connected to reef conservation efforts. The semi-submarine tour provided amazing views for those in our group who didn't want to snorkel."
            }
        ]
    },
    "29": {
        "id": "29",
        "title": "Bedarra Island Resort, Mission Beach",
        "image": "https://lh3.googleusercontent.com/proxy/NzauvuVbf-K7RiMxXMdXpq2Q9lTddvPG9S86mi2SHlIX5UlzDfGNaaVusia0OUvLUKDD_ouirUuRCRSt_njmb_E4gvJ0sbZC8KOHfLgtjvZvFL-lwwmxcQc6S_HSgfiV5TFCVpNjxNGQJPGlcYKKQdpGixVbG3E=s1360-w1360-h1020",
        "year": "2015",
        "summary": "Bedarra Island Resort offers luxurious seafront villas on a private tropical island, accommodating just 20 guests at a time. Each villa is designed to blend with the natural environment, using sustainable materials and featuring spacious indoor-outdoor living areas with spectacular ocean views. The interiors showcase contemporary Australian design with original indigenous artworks and handcrafted furniture. The resort operates on solar power and harvested rainwater, demonstrating how luxury and environmental responsibility can coexist.",
        "price_per_night": "$1,050",
        "location": "Australia",
        "amenities": ["Private plunge pool","Open-air bathroom","Stocked bar","Private beach access","Personal pantry service"],
        "rating": "4.9",
        "similar_bungalow_ids": ["28", "3", "1"],
        "activities": ["Snorkeling","Sea kayaking","Gourmet picnics","Rainforest walks"],
        "best_season": ["June", "July", "August", "September", "October", "November"],
        "reviews": [
            {
                "reviewer_name": "Emma Sutherland",
                "rating": "5.0",
                "date": "October 2023",
                "text": "Bedarra Island Resort is the epitome of eco-luxury. With only 20 guests at a time, it felt like we had our own private island. The indigenous artwork throughout our villa was museum-quality, and the open-air bathroom was a unique experience."
            },
            {
                "reviewer_name": "David Harrison",
                "rating": "4.8",
                "date": "September 2023",
                "text": "The personal pantry service meant our favorite drinks and snacks were always stocked. Taking a gourmet picnic hamper to a secluded beach that staff had set up just for us was an incredible touch of luxury and privacy."
            },
            {
                "reviewer_name": "Sophia Chen",
                "rating": "5.0",
                "date": "August 2023",
                "text": "The combination of rainforest walks and ocean activities gave us the perfect mix of adventure and relaxation. Learning that the entire resort operates on solar power and harvested rainwater made us feel good about our choice to stay here."
            }
        ]
    }
}
# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/popular_bungalows')
def popular_bungalows():
    popular_ids = ["5", "19", "27"]
    popular = []
    
    for id in popular_ids:
        if id in bungalows:
            popular.append(bungalows[id])
    
    return jsonify(popular)

@app.route('/search')
def search():
    query = request.args.get('q', '').strip().lower()
    if not query:
        return render_template('search.html', query="", results=[], count=0)
    
    results = []
    for bungalow in bungalows.values():
        if (query in bungalow['title'].lower() or 
            query in bungalow['summary'].lower() or 
            query in bungalow['location'].lower()):
            results.append(bungalow)
    results = sorted(results, key=lambda x: x['title'].lower())
    count = len(results)
    
    return render_template('search.html', query=query, results=results, count=count)


@app.route('/view/<id>')
def view(id):
    if id in bungalows:
        return render_template('view.html', bungalow=bungalows[id], bungalows=bungalows)
    return "Bungalow not found", 404

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.get_json()
        
        # Validate required fields
        if not data.get('title'):
            return jsonify({"error": "Title is required"}), 400
            
        # Generate new ID
        new_id = str(len(bungalows) + 1)
        
        # Add new bungalow
        data['id'] = new_id
        if 'reviews' not in data:
            data['reviews'] = []
        bungalows[new_id] = data
        
        return jsonify({"id": new_id})
        
    return render_template('add.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if id not in bungalows:
        return "Bungalow not found", 404
        
    if request.method == 'POST':
        data = request.get_json()
        
        # Validate required fields
        if not data.get('title'):
            return jsonify({"error": "Title is required"}), 400
            
        # Preserve ID and reviews
        data['id'] = id
        if 'reviews' not in data and 'reviews' in bungalows[id]:
            data['reviews'] = bungalows[id]['reviews']
        
        # Update bungalow
        bungalows[id] = data
        
        return jsonify({"success": True})
        
    return render_template('edit.html', bungalow=bungalows[id])

@app.route('/add_review/<id>', methods=['POST'])
def add_review(id):
    if id not in bungalows:
        return jsonify({"error": "Bungalow not found"}), 404
        
    data = request.get_json()
    
    # Validate required fields
    if not data.get('reviewer_name') or not data.get('rating') or not data.get('text'):
        return jsonify({"error": "All fields are required"}), 400
        
    # Initialize reviews list if it doesn't exist
    if 'reviews' not in bungalows[id]:
        bungalows[id]['reviews'] = []
        
    # Add the review to the bungalow
    bungalows[id]['reviews'].append(data)
    
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True, port=5001)