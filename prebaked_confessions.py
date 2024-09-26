prebaked_user_count = 20

confessions = [
    {
        "text" : "I secretly browse social media profiles of people I don't know and imagine what their lives are like.",
        "confession_id" : 0,
        "user_id" : 1,
        "timestamp" : "2024-01-01:19:00",
        "allow_comments" : True,
        "comments" : [
            {
                "user_id" : 2,
                "text": "wow!",
                "timestamp" : "2024-01-01:19:00",
            },
            {
                "user_id" : 3,
                "text" : "OMG!",
                "timestamp" : "2024-01-01:19:00",
            }
        ],
        "likes" : [2, 3, 4, 5],
    },
    {
        "text" : "I once created a fake online persona and had a long-distance relationship with someone for over a year.",
        "confession_id" : 1,
        "user_id" : 2,
        "timestamp" : "2024-03-04:14:32",
        "allow_comments" : True,
        "comments" : [
            {
                "user_id" : 5,
                "text": "What a horrible thing to do! That poor person must have been devastated!",
                "timestamp" : "2024-01-01:19:00",
            },
            {
                "user_id" : 6,
                "text" : "Hang on, OP doesn't say if the person ever found out.",
                "timestamp" : "2024-01-01:19:00",
            },
            {
                "user_id" : 7,
                "text" : "Exactly! Maybe OP was just bringing love to the world.",
                "timestamp" : "2024-01-01:19:00",
            }
        ],
        "likes" : [2, 5],
    },
    {
        "text" : "I often leave negative comments on online forums just to provoke a reaction from others.",
        "confession_id" : 2,
        "user_id" : 3,
        "timestamp" : "2024-02-15:10:16",
        "allow_comments" : False,
        "comments" : [],
        "likes" : [2, 3, 5],
    },
    {
        "text" : "I have a secret blog where I write about my deepest fears and insecurities, but I never share it with anyone.",
        "confession_id": 3,
        "user_id" : 4,
        "timestamp" : "2024-05-22:02:32",
        "allow_comments" : True,
        "comments" : [
            {
                "user_id" : 11,
                "text": "This is a great idea. You have to get things off your chest.",
                "timestamp" : "2024-01-01:19:00",
            },
            {
                "user_id" : 12,
                "text" : "This is so brave. I'd be too afraid that someone would find it!",
                "timestamp" : "2024-01-01:19:00",
            },
        ],
        "likes" : [2],
    },
    {
        "text" : "I frequently use a VPN to access blocked websites at work, even though it's against company policy.",
        "confession_id" : 4,
        "user_id" : 5,
        "timestamp" : "2024-04-13:09:16",
        "allow_comments" : True,
        "comments" : [
            {
                "user_id" : 14,
                "text": "Go for it! It's what I'm doing right now.",
                "timestamp" : "2024-01-01:19:00",
            },
            {
                "user_id" : 15,
                "text" : "Am I the only one who thinks this is like stealing? Aren't you supposed to be working?",
                "timestamp" : "2024-01-01:19:00",
            },
            {
                "user_id" : 16,
                "text" : "As long as the sites you're accessing aren't hurting anyone, I say no harm, no foul.",
                "timestamp" : "2024-01-01:19:00",
            }
        ],
        "likes" : [2, 3, 4, 5],
    },
    {
        "text": "Sometimes I fake being on a phone call to avoid talking to people.",
        "confession_id": 5,
        "user_id": 6,
        "timestamp": "2024-01-03:08:45",
        "allow_comments": True,
        "comments": [
            { 
                "user_id": 6, 
                "text": "I do this too!", 
                "timestamp": "2024-01-03:08:50" },
        ],
        "likes": [2, 4, 6, 7]
    },
    {
        "text": "I still sleep with a nightlight because I'm afraid of the dark.",
        "confession_id": 6,
        "user_id": 7,
        "timestamp": "2024-01-04:22:10",
        "allow_comments": True,
        "comments": [
            { 
                "user_id": 7, 
                "text": "Same!", 
                "timestamp": "2024-01-04:22:15" 
            },
            { 
                "user_id": 8, 
                "text": "You're not alone!", 
                "timestamp": "2024-01-04:22:20" 
            },
        ],
        "likes": [5, 6, 9, 10]
    },
    {
        "text": "I tell people I'm allergic to mushrooms just because I hate them.",
        "confession_id": 7,
        "user_id": 8,
        "timestamp": "2024-01-05:17:25",
        "allow_comments": True,
        "comments": [
            { 
                "user_id": 9, 
                "text": "LOL I do this with olives!", 
                "timestamp": "2024-01-05:17:30" }
        ],
        "likes": [2, 7, 8]
    },
    {
        "text": "I once lied on my resume and got the job. Still have it three years later.",
        "confession_id": 8,
        "user_id": 9,
        "timestamp": "2024-01-06:11:40",
        "allow_comments": True,
        "comments": [
            { 
                "user_id": 10, 
                "text": "Wow, that's bold!", 
                "timestamp": "2024-01-06:11:45", 
            }
        ],
        "likes": [1, 3, 4, 9]
    },
    {
        "text": "I use my pet as an excuse to leave events early.",
        "confession_id": 9,
        "user_id": 10,
        "timestamp": "2024-01-07:09:55",
        "allow_comments": True,
        "comments": [
            { 
                "user_id": 3, 
                "text": "Great idea!", 
                "timestamp": "2024-01-07:10:00" 
            }
        ],
        "likes": [2, 5, 8, 9]
    },
    {
        "text": "I haven't been to the dentist in over five years.",
        "confession_id": 10,
        "user_id": 11,
        "timestamp": "2024-01-08:18:20",
        "allow_comments": True,
        "comments": [
            {
                "user_id": 1, 
                "text": "Same here!", 
                "timestamp": "2024-01-08:18:25" 
            },
            { 
                "user_id": 4, 
                "text": "Yikes!", 
                "timestamp": "2024-01-08:18:30" 
            }
        ],
        "likes": [6, 10]
    },
    {
        "text": "I re-watch old TV shows when I'm stressed instead of trying something new.",
        "confession_id": 11,
        "user_id": 12,
        "timestamp": "2024-01-09:20:15",
        "allow_comments": True,
        "comments": [
            { 
                "user_id": 5, 
                "text": "Same, it's comforting!", 
                "timestamp": "2024-01-09:20:20" 
            }
        ],
        "likes": [1, 3, 6]
    },
    {
        "text": "I still have my ex's hoodie and wear it sometimes when I miss them.",
        "confession_id": 12,
        "user_id": 13,
        "timestamp": "2024-01-10:12:50",
        "allow_comments": True,
        "comments": [
            {
                "user_id": 2, 
                "text": "Wow, that's deep.", 
                "timestamp": "2024-01-10:12:55" 
            },
            { 
                "user_id": 6, 
                "text": "I can relate.", 
                "timestamp": "2024-01-10:13:00" 
            }
        ],
        "likes": [4, 7, 8]
    },
    {
        "text": "I pretend to like fancy food, but I'd rather have a burger and fries.",
        "confession_id": 13,
        "user_id": 14,
        "timestamp": "2024-01-11:16:45",
        "allow_comments": True,
        "comments": [
            {
                "user_id": 10, 
                "text": "Fancy food is overrated!", 
                "timestamp": "2024-01-11:16:50" 
            }
        ],
        "likes": [2, 3, 5, 9]
    },
    {
        "text": "I have a huge crush on my best friend's sibling but will never say anything.",
        "confession_id": 14,
        "user_id": 15,
        "timestamp": "2024-01-12:14:05",
        "allow_comments": True,
        "comments": [
            {
                "user_id": 7, 
                "text": "That's rough.", 
                "timestamp": "2024-01-12:14:10" 
            },
            { 
                "user_id": 9, 
                "text": "Oof, that's tough.", 
                "timestamp": "2024-01-12:14:15" 
            }
        ],
        "likes": [3, 8, 10]
    },
    {
        "text": "I told my partner I liked their cooking when I really hated it.",
        "confession_id": 15,
        "user_id": 16,
        "timestamp": "2024-01-13:11:35",
        "allow_comments": True,
        "comments": [
            {
                "user_id": 8, 
                "text": "LOL! Brave.", 
                "timestamp": "2024-01-13:11:40" 
            }
        ],
        "likes": [5, 6, 9]
    },
    {
        "text": "I sometimes fake being sick to get a day off.",
        "confession_id": 16,
        "user_id": 17,
        "timestamp": "2024-01-14:13:25",
        "allow_comments": True,
        "comments": [
            {
                "user_id": 10, 
                "text": "I've done this before!", 
                "timestamp": "2024-01-14:13:30" 
            }
        ],
        "likes": [2, 3, 4, 7]
    },
    {
        "text": "I tell my friends I'm busy, but I'm really just binge-watching TV shows.",
        "confession_id": 17,
        "user_id": 18,
        "timestamp": "2024-01-15:15:50",
        "allow_comments": True,
        "comments": [
            {
                "user_id": 6, 
                "text": "Same here!", 
                "timestamp": "2024-01-15:15:55" 
            }
        ],
        "likes": [1, 8, 10]
    },
    {
        "text": "I have a secret bank account my partner doesn't know about.",
        "confession_id": 18,
        "user_id": 19,
        "timestamp": "2024-01-16:09:40",
        "allow_comments": True,
        "comments": [
            {
                "user_id": 4, 
                "text": "Wow, that's risky!", 
                "timestamp": "2024-03-04:13:23"
            },
            {
                "user_id": 7, 
                "text": "Better to be safe than sorry", 
                "timestamp": "2024-03-05:18:27"
            },
            { 
                "user_id": 9, 
                "text": "My granny always did the same thing... well, she kept money under the mattress but still", 
                "timestamp": "2024-03-06:10:13"
            },
        ],
        "likes": [1, 8, 10]
    },
        {
        "text": "I keep a jar of candy at work and eat it all by myself, pretending it's for my coworkers.",
        "confession_id": 19,
        "user_id": 20,
        "timestamp": "2024-01-02:14:30",
        "allow_comments": True,
        "comments": [
            { 
                "user_id": 4, 
                "text": "LOL!", 
                "timestamp": "2024-01-02:14:35", 
            },
        ],
        "likes": [3, 5, 6]
    },
]

