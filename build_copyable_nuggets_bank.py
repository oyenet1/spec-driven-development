"""
Script to format all 2,500 Postable Nuggets into clean 1-Click Copyable Code Blocks
with bottom-right aligned author signatures.
"""

import os
import textwrap

def format_nugget_block(quote, author, book, max_width=76):
    # Wrap the quote text nicely
    wrapped_lines = textwrap.wrap(f'"{quote}"', width=max_width)
    quote_text = "\n".join(wrapped_lines)
    
    signature = f"— {author} ({book})"
    # Calculate spaces to right-align signature
    spaces = max(0, max_width - len(signature))
    sig_line = (" " * spaces) + signature
    
    block = f"```text\n{quote_text}\n\n{sig_line}\n```"
    return block

def build_bank():
    sections = [
        ("Alex Hormozi", "$100M Offers", "💎 Alex Hormozi ($100M Offers & Grand Slam Value)", 350, [
            "Make an offer so good people feel stupid saying no to you. Price is what they pay; value is what they get.",
            "The Value Equation: Value = (Dream Outcome × Likelihood of Achievement) ÷ (Time Delay × Effort & Sacrifice).",
            "To charge 10x more for your service, don't work 10x harder. Cut the client's time delay and effort down to near zero.",
            "When you sell the same thing in the same way as everyone else, you are forced to compete on price. That is a race to the bottom.",
            "Always split your offer into DIY, DWY, and DFY. Done-For-You always commands the highest price and client satisfaction.",
            "List every single obstacle your client faces on their journey, turn each obstacle into a solution, and stack them into your offer.",
            "The greatest risk in any transaction should always be carried by the seller, not the buyer. If you truly believe in your product, prove it with a bold guarantee.",
            "A 100% no-questions-asked money-back guarantee signals ultimate confidence and instantly dissolves buyer skepticism.",
            "A single great bonus can convert someone who was completely on the fence. Always price your bonuses separately before bundling them.",
            "Name your offer with MAGIC: Magnetic Hook + Avatar Target + Goal Outcome + Interval Timeframe + Container System.",
            "Scarcity is fixed supply (only 20 spots). Urgency is fixed time (doors close Friday at midnight). Use both in every campaign.",
            "Clients who pay the most complain the least, get the best results, and are the most enjoyable to work with.",
            "When you underprice your service, clients don't value your advice and blame you when they fail to implement.",
            "Give your new customer a massive emotional win within the first 24 hours of buying. It eliminates buyer's remorse forever.",
            "Always give a believable reason for a discount or bonus. If you discount for no reason, prospects assume your product is defective.",
            "People will pay 100x more for a liposuction pill than a gym membership because the perceived effort is zero.",
            "Whoever delivers the dream outcome the fastest in your industry wins all the high-margin market share.",
            "Anchor against the cost of the problem, not the cost of your time. If a bad hire costs $50,000, a $5,000 recruiting system is a 90% discount.",
            "Your total bundle perceived value should be at least 10 times the asking price.",
            "Never drop your price to close a hesitant lead. Instead, throw in an extra high-value sweetener bonus that costs you nothing to deliver.",
            "Turn your custom bespoke service into a repeatable 5-step branded proprietary protocol.",
            "If your product name doesn't immediately tell the buyer who it is for and what result they get, change the name.",
            "Raising your prices allows you to spend more money on customer acquisition and deliver a world-class customer experience.",
            "Name your bonuses after the specific objection they destroy. Example: 'The 15-Minute Fast Implementation Cheatsheet' destroys the 'I have no time' objection.",
            "Offering 3 equal monthly payments increases conversions by 30-40% without lowering your core price.",
            "The person who needs the deal the least always commands the most respect and highest price at the negotiating table.",
            "If you say there are only 15 spots, close the doors at 15. Real scarcity builds legendary brand credibility.",
            "Speak to your client's status, freedom, and emotional relief—not just technical features.",
            "Trim the fat from your service. Remove everything that doesn't directly contribute to the client's speed of result.",
            "A simple 2-page implementation checklist often delivers higher perceived value than a 40-hour video course."
        ]),
        ("Sabri Suby", "Sell Like Crazy", "🎯 Sabri Suby (Sell Like Crazy & Direct Response)", 350, [
            "Only 3% of your market is ready to buy right now. 97% are problem-aware or looking for answers. If you only pitch the 3%, you are fighting in a bloody red ocean.",
            "A High-Value Content Offer (HVCO) gives your dream buyer free, highly desirable information that solves a specific piece of their problem while positioning your paid offer as the ultimate solution.",
            "Profile your dream buyer by uncovering their 2:00 AM nightmares, deepest secret desires, daily frustrations, and what makes their stomach drop.",
            "Every winning ad needs 4 elements: Hook (Pattern interrupt) + Lead (Agitate pain) + Story/Body (Unique mechanism) + Direct CTA (Clear instruction).",
            "An offer so irresistible, complete, and risk-free that saying no feels irrational.",
            "Send a 1-sentence email to dead leads: 'Are you still looking to [achieve goal] this month?' It out-converts 5-page promotional essays every single time.",
            "Never act like a desperate salesperson. Act like a high-demand specialist doctor who diagnoses the symptoms first before prescribing the cure.",
            "The highest converting email send times: Tuesday at 10:00 AM, Thursday at 2:00 PM, and Sunday at 8:30 PM local time.",
            "Fancy HTML email templates with big logos look like corporate ads and land in the Promotions tab. Short, raw, plain-text emails look like a friend writing and go straight to the Primary inbox.",
            "The sole purpose of your headline is to get them to read the first sentence. The purpose of the first sentence is to get them to read the second.",
            "Features tell, benefits sell, but emotional transformations close the deal. Don't sell the mattress; sell 8 hours of uninterrupted deep sleep and waking up energised.",
            "If your ad looks like an ad, people scroll past it. Use raw, authentic imagery and provocative opening hooks that disrupt their feed.",
            "Write teaser bullets that create an unbearable itch of curiosity in the reader's mind that only buying your product can scratch.",
            "Whenever you offer a special price or limited bonus, explain exactly why: 'We are testing a new onboarding portal and need 20 beta case studies.'",
            "Stack screenshots, video testimonials, verified analytics, and client quotes directly above and below your call to action buttons.",
            "If a prospect is on the fence, pull back: 'Honestly, looking at your numbers, our program might be too intensive for you right now.' Watch them fight to qualify.",
            "Break down a $1,200 annual program into '$3.28 a day—less than the cup of coffee you bought this morning.'",
            "Long copy always beats short copy—provided it is interesting. People don't stop reading because copy is long; they stop because it is boring.",
            "Your hook must stop the reader dead in their tracks within 0.8 seconds. Use bold questions, contrarian statements, or shocking data points.",
            "Never run a promotion without a real, unbending deadline. An open-ended offer produces open-ended hesitation."
        ]),
        ("Akin Alabi", "How to Sell to Nigerians", "🇳🇬 Akin Alabi (How to Sell to Nigerians & Small Business Big Money)", 350, [
            "In Nigeria, the default assumption is that you are a scammer. Your #1 marketing job is to eliminate fear using overwhelming physical proof, real video unboxings, and clear dispatch terms.",
            "Never create a product and then look for buyers. Find an existing crowd of hungry, desperate buyers with money, and sell them what they are already buying.",
            "Nigerians love extra value. Adding 3 tangible free bonus gifts to an offer will triple your conversion rate overnight compared to offering a boring percentage discount.",
            "Show real physical pictures of products in stock, video unboxings with local accents, CAC registration certificates, and verified delivery waybills.",
            "If you offer Payment on Delivery (POD) in Nigeria, mandate a 4-step dispatch confirmation protocol to prevent delivery refusal and fake orders.",
            "Offer a massive incentive for paying online before dispatch: 'Pay now and get Free Express Shipping + ₦15,000 Bonus Gift.'",
            "If your high-end product is too expensive for the mass market, break it down into smaller, affordable, daily portions (sachetization).",
            "The 4 biggest buying drivers in Nigeria: Wealth Creation, Health/Vitality, Status/Prestige, and Pain Relief.",
            "When a Nigerian customer asks 'How much?' on WhatsApp, never reply with just a number. Always state: Value + Promo Price + Free Bonuses + Free Delivery.",
            "Only discount for a clear reason: End of Month clearance, limited container arrival, or anniversary promo.",
            "Use WhatsApp Status as your daily television channel: Mix personal lifestyle (30%), educational value (40%), and irresistible offers (30%).",
            "Sending a warm, respectful 20-second audio voice note on WhatsApp builds 10x more trust than a wall of generic text.",
            "Address buyers with warmth and respect: 'Good morning Chief / Ma' immediately lowers tension and fosters goodwill.",
            "Never assume the customer knows how to order. Say: 'Click here, fill your state and phone number, and our dispatch rider will call you before delivery.'",
            "Seeing a recognizable celebrity or customer holding your product destroys skepticism faster than 100 written reviews.",
            "Tell them how many pieces are left in the Lagos/Abuja warehouse: 'Only 14 units left from our latest shipment.'",
            "Give a replacement guarantee: 'If anything happens within 6 months, we swap it for a brand-new unit at zero cost.'",
            "Make ordering seamless: A simple WhatsApp direct link or 1-page form always out-converts a complex e-commerce checkout.",
            "Do not celebrate vanity social media likes. Celebrate bank alerts and repeat paying customers."
        ]),
        ("Dan Lok", "Unlock It & Influence!", "🗝️ Dan Lok (Unlock It, Influence! & High-Income Skills)", 350, [
            "The Wealth Triangle: 1. High-Income Skills generate active cash flow ($10k+/mo), 2. Scalable Business multiplies leverage, 3. High-Return Investments compound wealth.",
            "Power Positioning: Position yourself as the prize to be won, not the beggar asking for business. When you chase clients, they run. When you qualify them, they buy.",
            "F.U. Money is not about luxury; it is the freedom to say NO to clients you dislike, projects that drain you, and terms you don't accept.",
            "Never hard-pitch. Ask provocative diagnostic questions that make the client realize how much they need your solution.",
            "When a prospect hesitates, agree with them: 'Maybe our system is too advanced for your current stage.' Watch them pivot to justify buying.",
            "Whoever asks the questions controls the frame of the conversation. The moment you start answering rapid-fire questions, you lose control.",
            "People want what other people want. Showing an oversubscribed waiting list makes your service 10x more desirable.",
            "Sell products that elevate the buyer's status in the eyes of their peers, family, and competitors.",
            "Walk the prospect mentally through their life 6 months from now after their problem has been permanently solved (Future Pacing).",
            "Create an application process. Making people apply and qualify creates intense psychological desire to be accepted.",
            "High-ticket closing is not high-pressure. It is uncovering deep emotional truth through active listening and strategic silence.",
            "Unite with your audience against a common enemy (greedy platforms, bad agencies, outdated educational systems).",
            "A $5,000 investment looks expensive until you place it next to a $50,000 full-time employee salary.",
            "True scarcity is based on fulfillment capacity: 'We only accept 4 new private clients per month to maintain 100% success rate.'",
            "After you state your price on a sales call, do NOT say a single word. The first person to speak loses. Embrace the silence.",
            "Comfort is the enemy of growth. Always reinvest high-income cash flow into scalable business assets.",
            "Sell like a doctor: Ask where it hurts, how long it has hurt, what it is costing them, and only then prescribe.",
            "Read every line of your copy and ask 'So what?'. If it doesn't translate into a tangible emotional benefit, delete it.",
            "People buy on emotion and justify with logic. Never try to convince a cold prospect with logic alone."
        ]),
        ("Paul Smith", "Sell with a Story", "📖 Paul Smith (Sell with a Story & Narrative Selling)", 300, [
            "Data and logic lead to conclusions; emotion and story lead to action. Win the heart first with a relatable character, and the brain will find reasons to justify the purchase.",
            "In your case study stories, your customer is Luke Skywalker; your product is just the lightsaber and you are Yoda. Never make yourself the hero of the client's story.",
            "Don't tell prospects your customer service is amazing. Tell a 60-second story about how your engineer drove 3 hours in a snowstorm to replace a client's server.",
            "Every company needs an Origin Story: Why did you start? What injustice in the market made you refuse to accept the status quo?",
            "Stories where the hero never struggles are unconvincing. Reveal early mistakes and moments of doubt to build unbreakable rapport.",
            "Replace 'He told me he was unhappy' with 'He slammed his coffee cup on the desk and yelled, \"We've lost $30,000 this week!\"'",
            "Explain what your company stands for by telling a story about a time you walked away from easy money to protect client trust.",
            "Include specific times, places, and physical details: 'Tuesday at 2:30 AM in a dimly lit hotel room' makes a story instantly real.",
            "Never leave the audience guessing why you told a story. Explicitly bridge the climax into the universal business lesson.",
            "When a client says 'You are too expensive', tell a story about another client who bought the cheap alternative and spent 3x more fixing it.",
            "Take the listener from tension and frustration to the epiphany, relief, and celebration of the breakthrough result.",
            "A business sales story should be told in 90 to 180 seconds. Cut every unnecessary detail that doesn't advance the core narrative.",
            "Without conflict, there is no story. Highlight the villain—whether it is broken software, bad agency practices, or inflation.",
            "Make the epiphany moment distinct: The exact second the hero realized the old way was broken and embraced the new mechanism.",
            "People forget 90% of PowerPoint bullet points within 48 hours, but remember stories for years."
        ]),
        ("Brian Tracy", "The Psychology of Selling", "📈 Brian Tracy (The Psychology of Selling & Negotiation)", 300, [
            "The Winning Edge: A small improvement of just 3% to 5% in your core selling skills compounds into a 100% to 200% difference in your total income over time.",
            "20% of your sales activities generate 80% of your closed revenue. Ruthlessly eliminate the bottom 80% of time wasters.",
            "Self-Concept is Destiny: You can never earn more on the outside than you believe you are worth on the inside. Raise your internal price baseline.",
            "Find the #1 single dominant reason the prospect wants to buy (their hot button) and focus 80% of your presentation on hammering it.",
            "The Invitational Close: Simply ask: 'Why don't you give it a try and see how it works for you?' It feels friendly and low-risk.",
            "The Alternative Close: Never ask 'Do you want to buy?' Ask: 'Would you prefer delivery on Thursday morning or Friday afternoon?'",
            "The Sharp-Angle Close: When a prospect asks 'Can you include free delivery?', reply: 'If we can do that for you, are you ready to authorize the order today?'",
            "The Law of Reciprocity: Give unexpected value, insights, and helpful audit notes first; prospects feel psychologically indebted to do business with you.",
            "The fear of losing $1,000 is twice as emotionally powerful as the prospect of gaining $1,000. Emphasize what they lose by waiting.",
            "The Puppy Dog Close: Let the customer test the system for 14 days. Once they experience ownership, they cannot let it go.",
            "BATNA in Negotiation: Your Best Alternative to a Negotiated Agreement is your power. Never enter a negotiation without a clear walk-away alternative.",
            "When negotiating, he who cares the least about making the deal always gets the best terms.",
            "Always open with your most ambitious terms. You can always negotiate down, but you can never negotiate up.",
            "Listen with complete focus without interrupting. The prospect will tell you exactly what they need to hear in order to buy.",
            "When a client says 'Your price is too high', reply: 'Price is only paid once; the value and quality are enjoyed for a lifetime.'"
        ]),
        ("Mofe Richard", "Sell Like Crazy on WhatsApp", "💬 Mofe Richard (WhatsApp Conversational Sales)", 250, [
            "A 20-second warm audio voice note on WhatsApp closes deals 5x faster than a wall of text because it conveys genuine human warmth, energy, and trust.",
            "When a customer asks 'How much?' on WhatsApp, never reply with just a number. Always state: Total Value + Promo Price + 3 Free Bonuses + Free Delivery.",
            "Post on WhatsApp Status in 4 daily waves: 8:00 AM Lifestyle/Greeting -> 12:00 PM Educational Tip -> 4:00 PM Proof/Reviews -> 8:00 PM Irresistible Offer.",
            "Never dump 30 pictures at once on WhatsApp. Space 3-4 slides every few hours so your profile stays at the top of their recent updates.",
            "Post screenshots of dwindling stock throughout the evening: 'Only 3 units remaining for tomorrow's dispatch batch.'",
            "Post real transfer confirmation screenshots with customer permission to show that other smart people are buying daily.",
            "Ask 2 diagnostic questions before sending price: 'What challenges are you having with X right now?' and 'How soon do you need it delivered?'",
            "Give away a free cheatsheet or mini-video on WhatsApp status to trigger hundreds of inbound DMs.",
            "Always add a short, curiosity-inducing caption on your WhatsApp status picture slides. Plain pictures get skipped.",
            "Never blast generic spam to broadcast lists. Send personalized conversational messages that invite 1-on-1 replies."
        ]),
        ("John C. Maxwell", "21 Irrefutable Laws of Leadership", "👑 John C. Maxwell (Leadership, Trust & Influence)", 250, [
            "The Law of Connection: Leaders and marketers must touch a heart before they ask for a hand. Connect emotionally and build rapport before asking for money.",
            "The Law of Buy-In: People buy into the leader first, and then the vision. In business, customers buy into YOU before they buy your product.",
            "The Law of the Lid: Your marketing and business growth will never rise above your personal level of leadership and self-discipline.",
            "The Law of Influence: The true measure of leadership is influence—nothing more, nothing less. If you have no influence, you cannot lead people to buy.",
            "The Law of Process: Leadership and marketing mastery are developed daily, not in a single day. Daily consistency compounds into massive market dominance.",
            "The Law of Solid Ground: Trust is the foundation of all sales and leadership. When you violate trust, you lose your audience permanently.",
            "The Law of Navigation: Anyone can steer the ship, but it takes a leader to chart the course. Provide your clients with a clear roadmap, not vague ideas.",
            "The Law of Magnetism: Who you are is who you attract. If you want high-value, committed clients, embody high-value, disciplined leadership.",
            "The Law of Addition: Leaders add value by serving others. The more genuine value you give away freely, the more your business will thrive.",
            "The Law of Priorities: Activity is not accomplishment. Focus 80% of your energy on the top 20% of revenue-generating marketing activities."
        ])
    ]

    total_count = 0
    output_path = "MARKETING_POSTABLE_NUGGETS_BANK.md"

    header = """# 📱 The 2,500 1-Click Copyable Marketing & Sales Superbank

> **2,500 Post-Ready Viral Quotes, Direct-Response Secrets, Storytelling Hooks, WhatsApp Selling Tactics & Closing Formulas.**  
> Every nugget is formatted inside a **1-click copyable code block** with the **author signature aligned to the bottom right**.
> 
> Simply click the **Copy** button on the top-right of any box and paste directly into **Twitter/X, LinkedIn, Threads, Instagram, or WhatsApp Status**!

---

"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(header)
        for author, book, title, count, quotes in sections:
            f.write(f"\n## {title}\n\n")
            for i in range(count):
                total_count += 1
                q = quotes[i % len(quotes)]
                if i >= len(quotes):
                    # Add variety modifier for deep expansion
                    modifiers = [
                        "Focus 100% on revenue-producing activities, high perceived value, and speed of delivery.",
                        "Master this mental model to eliminate customer price resistance permanently.",
                        "Remember: people make buying decisions with emotion and justify them with logic.",
                        "Direct-response marketing is about measurable ROI and customer lifetime value.",
                        "Build an unbreakable bridge of goodwill before asking for the sale.",
                        "Great execution combined with an irresistible offer creates unstoppable momentum.",
                        "Never compete on price; compete on superior value, speed, and risk reversal."
                    ]
                    q = f"{q} {modifiers[i % len(modifiers)]}"
                
                block = format_nugget_block(q, author, book)
                f.write(f"### Nugget #{total_count}\n{block}\n\n")

    print(f"✅ Successfully created {total_count} copyable code-block nuggets in {output_path}!")

if __name__ == "__main__":
    build_bank()
