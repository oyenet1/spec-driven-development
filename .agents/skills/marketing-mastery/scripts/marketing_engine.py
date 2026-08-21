#!/usr/bin/env python3
"""
Marketing Mastery Engine & CLI Generator
Implements core frameworks from:
- Sabri Suby ("Sell Like Crazy")
- Alex Hormozi ("$100M Offers")
- Paul Smith ("Sell with a Story")
- Akin Alabi ("How to Sell to Nigerians" & "Small Business Big Money")
- Dan Lok ("Influence!", "Unlock It", "F.U. Money")
- Brian Tracy ("The Psychology of Selling" & "Negotiation")
- Mofe Richard ("Sell Like Crazy on WhatsApp")
"""

import sys
import os
import argparse

def generate_17_step_sales_letter(avatar, dream_outcome, timeframe, obstacle, mechanism, price, anchor_price, guarantee_days, lang="en"):
    print("=" * 80)
    print(f"SABRI SUBY'S 17-STEP SECRET SELLING SYSTEM ({lang.upper()})")
    print("=" * 80)
    
    if lang.lower() in ["es", "spanish", "español"]:
        template = f"""
[PASO 1: LLAMAR A TU AUDIENCIA]
Atención {avatar} que están hartos de {obstacle}...

[PASO 2: CAPTAR LA ATENCIÓN - GRAN PROMESA]
Cómo {dream_outcome} en {timeframe} (Incluso Si {obstacle}) — ¡100% Garantizado!

[PASO 3: RESPALDAR LA PROMESA - SUBTÍTULO]
Descubre el comprobado {mechanism} que permite a {avatar} conseguir resultados predecibles sin dolores de cabeza ni dinero desperdiciado.

[PASO 4: CREAR INTRIGA IRRESISTIBLE - PUNTOS CLAVE]
Dentro de este sistema revolucionario descubrirás:
• La razón #1 por la cual el 95% de {avatar} fracasa al intentar {dream_outcome}...
• La "Palanca Oculta" en {mechanism} que reduce tu esfuerzo a la mitad...
• Cómo eliminar {obstacle} para siempre usando nuestro protocolo de 3 pasos...

[PASO 5: ILUMINAR EL PROBLEMA]
Seamos honestos: Intentar {dream_outcome} es agotador.
Has probado guías genéricas y cursos caros, solo para terminar en el mismo lugar. Cada día batallando contra {obstacle} es dinero y tranquilidad que pierdes.

[PASO 6: REVELAR LA SOLUCIÓN]
Por eso creamos {mechanism}. Ataca la causa raíz de {obstacle} y te da un camino claro hacia {dream_outcome}.

[PASO 7: CREDENCIALES Y PRUEBAS]
Probado en cientos de negocios con testimonios reales y resultados medibles.

[PASO 8: BENEFICIOS (CARACTERÍSTICA -> BENEFICIO)]
• Automatización Total --> Recuperas horas libres cada semana.
• Plan Paso a Paso --> Cero dudas, sabes exactamente qué hacer cada día.

[PASO 9: PRUEBA SOCIAL]
"Antes de usar {mechanism}, estaba totalmente abrumado por {obstacle}. ¡En {timeframe}, mis resultados se duplicaron!" — Cliente Verificado

[PASO 10: LA OFERTA DE EL PADRINO]
Acceso completo e ilimitado a todo el sistema {mechanism} y plantillas de ejecución.

[PASO 11: BONOS EXCLUSIVOS]
• Bono #1: Bóveda de Plantillas de Rápida Implementación (Valor: $497 USD)
• Bono #2: Guión de Cierre de Alto Valor (Valor: $997 USD)

[PASO 12: VALOR TOTAL ACUMULADO]
Valor Total Combinado: ${anchor_price} USD

[PASO 13: REVELAR EL PRECIO]
Hoy no pagarás ${anchor_price}. ¡Todo es tuyo por una única inversión de ${price} USD!

[PASO 14: ESCASEZ GENUINA]
Estrictamente limitado a 20 plazas para garantizar soporte personalizado.

[PASO 15: GARANTÍA DE RIESGO CERO]
Garantía Incondicional de {guarantee_days} Días: Si no alcanzas {dream_outcome}, te devolvemos el 100% de tu dinero.

[PASO 16: LLAMADO A LA ACCIÓN (CTA)]
Haz clic en el botón de abajo para asegurar tu lugar con descuento:
>>> [ ASEGURAR MI LUGAR AHORA >> ] <<<

[PASO 17: P.D. ADVERTENCIA FINAL]
P.D. Si estás listo para dejar atrás {obstacle} y lograr {dream_outcome} en {timeframe}, toma acción hoy mientras los bonos y la garantía están vigentes.
"""
    elif lang.lower() in ["pcm", "pidgin", "nigerian-pidgin"]:
        template = f"""
[STEP 1: CALL OUT AUDIENCE]
Attention all {avatar} wey don tire for {obstacle}...

[STEP 2: BIG PROMISE HEADLINE]
How to {dream_outcome} inside {timeframe} (Even If {obstacle}) — 100% Guaranteed!

[STEP 3: BACK UP PROMISE - SUBHEAD]
Discover the original {mechanism} wey dey help {avatar} get steady results without any stress, wasted money, or sleepless nights.

[STEP 4: BULLETS WEY DEY SHOCK]
Inside this system, you go discover:
• The #1 reason why 95% of {avatar} dey fail when dem wan {dream_outcome}...
• The secret inside {mechanism} wey dey cut your hard work by half...
• How to kill {obstacle} once and for all with 3 simple steps...

[STEP 5: SHINE LIGHT FOR THE PROBLEM]
Make we talk true: To {dream_outcome} no easy at all.
You fit don try many fake methods and courses, but nothing work. Every day wey you spend dey fight {obstacle} na money and peace of mind wey dey go.

[STEP 6: INTRODUCE THE SOLUTION]
Na why we build {mechanism}. E dey attack the real root of {obstacle} and show you clear road to {dream_outcome}.

[STEP 7: PROOF AND TESTIMONY]
We don test am with hundreds of businesses across Nigeria with real bank alert and video proofs.

[STEP 8: VALUE & BONUSES]
• Bonus #1: Fast-Action Template Vault (Value: ₦150,000)
• Bonus #2: WhatsApp Closing Scripts (Value: ₦250,000)

[STEP 9: THE GODFATHER PRICE]
Total Value na ${anchor_price}, but today na only ${price} you go pay!

[STEP 10: 100% MONEY-BACK GUARANTEE]
Try am for {guarantee_days} days. If you no get {dream_outcome}, we go refund your 100% money back without any drama.

[STEP 11: CALL TO ACTION]
Click the link now make you claim your slot before promo end:
>>> [ I WANT MY COPY NOW >> ] <<<
"""
    else:
        template = f"""
[STEP 1: CALL OUT YOUR AUDIENCE]
Attention {avatar} who are fed up with {obstacle}...

[STEP 2: DEMAND ATTENTION - BIG PROMISE HEADLINE]
How to {dream_outcome} in {timeframe} (Even If {obstacle})—Guaranteed!

[STEP 3: BACK UP BIG PROMISE - SUBHEADLINE]
Discover the battle-tested {mechanism} that allows {avatar} to achieve predictable results without the usual headaches, wasted money, or sleepless nights.

[STEP 4: CREATE IRRESISTIBLE INTRIGUE - FASCINATING BULLETS]
Inside this breakthrough system, you'll discover:
• The #1 reason why 95% of {avatar} fail when trying to {dream_outcome} (and what the top 1% do instead)...
• The "Hidden Lever" in {mechanism} that slashes your effort in half while doubling your speed...
• How to eliminate {obstacle} permanently using our simple 3-step protocol...
• The counter-intuitive secret to scaling your results without working 60-hour weeks...
• Real-life case studies of people just like you who transformed their results in under {timeframe}...

[STEP 5: SHINE A FLOODLIGHT ON THE PROBLEM]
Let's be honest: Trying to {dream_outcome} is brutal.
You've probably tried generic guides, hired expensive consultants, or spent months grinding—only to end up right back where you started.
Every day you spend battling {obstacle} is another day of lost revenue, stress, and anxiety. It feels like you're running on a hamster wheel that never stops.

[STEP 6: PROVIDE THE SOLUTION]
That's exactly why we engineered {mechanism}.
Unlike other generic methods that treat the symptoms, {mechanism} attacks the root cause of {obstacle}, giving you a clear, step-by-step path to {dream_outcome}.

[STEP 7: SHOW YOUR CREDENTIALS & PROOF]
We didn't just invent this overnight. Over the past several years, our system has been deployed across hundreds of businesses, generating proven track records, measurable transformations, and verified client case studies.

[STEP 8: DETAIL THE BENEFITS (2-COLUMN BENEFIT MATRIX)]
• Feature: Automated Framework  --> Benefit: You get hours back every week to focus on high-level growth.
• Feature: Step-by-Step Blueprint --> Benefit: Zero guesswork—you know exactly what to do every morning.
• Feature: Direct Support & Audits --> Benefit: Never get stuck again; our experts review your work.

[STEP 9: SOCIAL PROOF STACKING]
"Before using {mechanism}, I was completely overwhelmed by {obstacle}. Within {timeframe}, my results doubled!" — Verified Client Review

[STEP 10: THE GODFATHER OFFER]
When you join today, you get complete, unrestricted access to the entire {mechanism} suite, including all modules, execution templates, and live implementation support.

[STEP 11: HIGH-VALUE SWEETENER BONUSES]
• Bonus #1: The Fast-Action Implementation Cheatsheet (Value: $497)
• Bonus #2: The Objection-Crushing Script Vault (Value: $997)
• Bonus #3: Private Q&A Teardown Vault (Value: $497)

[STEP 12: THE TOTAL VALUE STACK]
Total Value of Core System + All Bonuses: ${anchor_price}

[STEP 13: REVEAL YOUR PRICE]
You won't pay anywhere near ${anchor_price}.
Today, you get everything for a single investment of just ${price}!

[STEP 14: INJECT GENUINE SCARCITY]
To ensure our team can provide white-glove onboarding and personal support, this cohort is strictly limited to 20 participants. Once the countdown timer hits zero or spots fill, doors close.

[STEP 15: GIVE A POWERFUL RISK-REVERSAL GUARANTEE]
You have our 100% Ironclad {guarantee_days}-Day Money-Back Guarantee. Take the entire system, implement it, and see the results for yourself. If you don't hit {dream_outcome}, email us for a full 100% refund. You carry zero risk.

[STEP 16: CALL TO ACTION (CTA)]
Click the button below right now to lock in your discounted rate and claim your bonuses before spots run out:
>>> [ CLAIM YOUR SPOT NOW >> ] <<<

[STEP 17: P.S. WARNING & REMINDER]
P.S. Remember: Doing the same thing over and over while expecting different results is the definition of insanity. If you're ready to overcome {obstacle} and finally {dream_outcome} in {timeframe}, claim your spot now while the guarantee and bonuses are active.
"""
    print(template)


def generate_power_4_ad(avatar, pain, solution_name, dream_outcome, link_url):
    print("=" * 80)
    print("POWER 4 META AD COPY (SABRI SUBY METHOD)")
    print("=" * 80)
    
    ad_copy = f"""
[HOOK / HEADLINE]
Attention {avatar}: Still struggling with {pain}? Stop scrolling.

[THE LEAD]
Most people in our industry are doing it completely backwards.
They grind 14 hours a day, test 10 different gimmicks, and still end up burned out and frustrated.

[THE STORY & AGITATION]
I used to think the only way to achieve {dream_outcome} was to sacrifice all my free time.
Then I uncovered the core flaw in traditional advice: It relies on hope instead of a proven direct-response mechanism.

That's when we built {solution_name}.
Instead of relying on guesswork, it gives you a step-by-step roadmap to achieve {dream_outcome} with predictable consistency.

[THE CALL TO ACTION]
We've documented the entire framework in a free, high-value guide.

Grab your copy for 100% free before this promotion expires:

👉 Tap here to download now: {link_url}
"""
    print(ad_copy)


def generate_story_ad(character, obstacle, discovery_moment, transformation, lesson, cta_link):
    print("=" * 80)
    print("HIGH-CONVERTING STORY AD (PAUL SMITH & SABRI SUBY FRAMEWORK)")
    print("=" * 80)
    
    story_ad = f"""
[STORY HOOK]
Two years ago, {character} was on the verge of quitting.

[CONTEXT & AGITATION]
It was 2:30 AM on a freezing Tuesday. {character} was sitting alone at the kitchen table, staring at a mountain of bills and a spreadsheet that just didn't make sense.
The problem? {obstacle}.

Every guru said: "Just work harder. Post more content. Cold message 100 people a day."
So {character} tried it. 14-hour days. Zero family time. And almost nothing to show for it except exhaustion and anxiety.

[THE EPIPHANY / CLIMAX]
Then, {discovery_moment}.

Instead of chasing clients and competing in the crowded 3% market, we flipped the script.
We deployed a simple direct-response mechanism that brought pre-qualified leads directly to us.

[THE TRANSFORMATION]
Within 60 days:
✓ {transformation}
✓ The stress and late-night panic disappeared.
✓ Operations became predictable and profitable.

[THE UNIVERSAL LESSON]
Here's what this taught us: {lesson}

[CALL TO ACTION]
If you're facing {obstacle} and want to see the exact step-by-step system we used, we've broken it down inside our free case study blueprint.

👉 Click here to read the full case study: {cta_link}
"""
    print(story_ad)


def refine_user_story(raw_story, hero_name, business_lesson, offer_cta):
    print("=" * 80)
    print("STORY REFINEMENT ENGINE (PAUL SMITH 8-PART STORY SPINE)")
    print("=" * 80)
    print("ORIGINAL RAW STORY INPUT:")
    print(f"\"{raw_story}\"\n")
    print("-" * 80)
    print("REFINED 8-PART HIGH-IMPACT SALES STORY:")
    print("-" * 80)

    refined = f"""
1. THE HOOK (Transition In):
"Can I share a quick 60-second story about what happened to {hero_name}? Because it reveals the exact trap most people fall into..."

2. CONTEXT (Time, Place & Desire):
A while back, {hero_name} was determined to break through to the next level. On paper, everything looked fine, but behind the scenes, there was an invisible bottleneck.

3. THE CHALLENGE (The Disruption):
Suddenly, reality hit. The standard strategies stopped working. Costs went up, response rates dried up, and {hero_name} found themselves working twice as hard for half the results.

4. THE CONFLICT & STRUGGLE (Visceral Agony):
{hero_name} thought: "If this continues, I'll have to shut down operations." They tried every traditional workaround, spent money on courses and generic tools, but the needle didn't budge. The stress was palpable.

5. THE CLIMAX & EPIPHANY (The Breakthrough):
That's when {hero_name} discovered the missing link: It wasn't about working more hours; it was about shifting from passive hope to an active direct-response mechanism.

6. THE RESOLUTION (Measurable Transformation):
The moment that shift happened, results followed rapidly. Inefficiency vanished, revenue stabilized, and confidence was restored.

7. THE BUSINESS LESSON:
"{business_lesson}"

8. RECOMMENDED ACTION (Transition Out):
"That's why I strongly recommend taking a look at our framework today: {offer_cta}"
"""
    print(refined)


def generate_video_ad_script(hook, pain_point, solution_name, proof_point, cta_command):
    print("=" * 80)
    print("HIGH-CONVERTING DIRECT-RESPONSE VIDEO AD SCRIPT (60-90s)")
    print("=" * 80)
    
    script = f"""
[0:00 - 0:05] HOOK (Pattern Interrupt & Avatar Callout)
• Visual: Creator looks directly into camera with high energy, holding a prop or pointing at screen.
• Text on Screen: ⚠️ STOP SCROLLING IF YOU DEAL WITH {pain_point.upper()}
• Audio / Dialogue: "If you're a business owner still struggling with {pain_point}, you need to hear this right now."

[0:05 - 0:20] AGITATE THE PAIN & BUST THE MYTH
• Visual: Cut to B-roll of stressed person at desk, or screen recording of broken workflows.
• Text on Screen: Why traditional methods fail ❌
• Audio / Dialogue: "Most people think the answer is to work longer hours or burn more money on ads. But here's the brutal truth: Trying to fix this with old methods is like trying to fill a bucket with a hole in the bottom."

[0:20 - 0:45] INTRODUCE UNIQUE MECHANISM & PROOF
• Visual: Creator demonstrates {solution_name} on laptop or iPad. Quick cut to verified customer testimonials.
• Text on Screen: The New Framework ✅ | {proof_point}
• Audio / Dialogue: "That's why we engineered {solution_name}. Instead of guessing, it gives you a predictable, step-by-step system. Just like our client who achieved {proof_point} in record time."

[0:45 - 1:00] THE GODFATHER OFFER & DIRECT CTA
• Visual: 3D mockup of the guide/training + animated finger pointing down to CTA button.
• Text on Screen: Download 100% Free 👉 Tap Link Below
• Audio / Dialogue: "Right now, you can get our complete step-by-step blueprint 100% free. Click the link right below this video, enter your details, and get instant access. {cta_command}!"
"""
    print(script)


def generate_ai_video_director_scenes(product_name, target_audience, duration_seconds=60, more_info=""):
    print("=" * 80)
    print("HOLLYWOOD-GRADE AI FILM DIRECTOR — 10-SECOND CONTINUOUS SCENE ENGINE")
    print("=" * 80)
    
    num_scenes = max(1, duration_seconds // 10)
    
    # 1. Master Film Continuity Anchor
    hero_char = f"32-year-old confident {target_audience} hero protagonist, natural expressive face, stylish contemporary wardrobe (navy-blue fitted linen button-up shirt, silver wristwatch), consistent hair and facial features across every angle"
    master_set = "Modern creative loft studio, rich walnut wood executive workstation, warm ambient architectural lighting, large industrial window with natural daylight, subtle indoor green plants, glass brainstorming board in background"
    camera_kit = "ARRI Alexa Mini LF, Cooke Anamorphic/i 35mm & 50mm lenses, natural cinematic 24fps motion blur, Kodak Vision3 500T 35mm film grain, DaVinci Resolve film color grade (warm golden skin tones, rich deep contrast, subtle teal shadows)"

    print(f"🎬 FILM PROJECT: {product_name}")
    print(f"🎯 TARGET AUDIENCE: {target_audience}")
    print(f"⏱️ TOTAL RUNTIME: {duration_seconds} Seconds ({num_scenes} Continuous 10s Scenes — ONE Single Film)")
    if more_info:
        print(f"💡 SPECIAL OFFER / DETAILS: {more_info}")
    
    print("\n" + "=" * 80)
    print("🔒 [MASTER FILM CONTINUITY ANCHOR — LOCKED FOR ALL SCENES]")
    print("=" * 80)
    print(f"• HERO CHARACTER: {hero_char}")
    print(f"• ENVIRONMENT & SET: {master_set}")
    print(f"• CAMERA & OPTICS: {camera_kit}")
    
    print("\n" + "=" * 80)
    print("🎙️ [UNBROKEN MASTER SCRIPT — 60-SECOND CONTINUOUS VOICE FLOW]")
    print("=" * 80)
    print(f'"{target_audience}, if you are tired of burning time and money on broken methods that leave you exhausted, listen closely. Traditional advice tells you to grind 16 hours a day, but that only leads to burnout. That is why we engineered {product_name}—a proven, automated framework that attacks the root problem directly. Our clients are cutting their workload in half while doubling their output with predictable consistency. When you join today, you get the complete master toolkit plus exclusive bonuses, backed by our 100% money-back guarantee. Click the link below right now and claim your free blueprint before this limited promotion ends."')
    print("=" * 80)

    scenes_data = [
        {
            "num": 1,
            "time": "0:00 - 0:10",
            "phase": "SCENE 1: THE PATTERN INTERRUPT HOOK",
            "camera": "Extreme Close-Up (ECU) fast push-in to Medium Close-Up (MCU). 35mm Cooke Anamorphic, f/1.8 shallow depth of field, 24fps film motion blur.",
            "lighting": "High-contrast dynamic volumetric rim lighting with subtle warm lens flare entering from window.",
            "prompt": f"Cinematic 4K film shot, fast camera push-in towards {hero_char}, looking directly into lens in {master_set}, intense passionate expression, speaking directly to viewer with authority, volumetric light rays, shot on {camera_kit} --ar 9:16 --motion 6",
            "vo": f"If you're a {target_audience} still struggling to get consistent results, stop scrolling right now and listen closely.",
            "ost": f"⚠️ ATTENTION {target_audience.upper()}",
            "sfx": "Sub-bass boom impact at 0:00, followed by an energetic, driving modern tech baseline.",
            "match_cut": "Ending frame shows hero gesturing towards the workstation screen. Camera finishes moving inward.",
            "transition": "Match cut to over-the-shoulder angle at the exact same workstation (Scene 2)."
        },
        {
            "num": 2,
            "time": "0:10 - 0:20",
            "phase": "SCENE 2: THE 2:00 AM NIGHTMARE & AGITATION",
            "camera": "Over-the-shoulder medium tracking shot at the SAME desk. 50mm cinema prime lens, creamy bokeh.",
            "lighting": "Moody low-key lighting in the same loft set, blue screen glow illuminating hero's face and hands.",
            "prompt": f"Cinematic 4K film shot, over-the-shoulder tracking shot of the SAME {hero_char} sitting at the exact same desk in {master_set}, reviewing stressful complex charts on computer screen, looking frustrated by outdated workflows, moody blue and amber rim lighting, shot on {camera_kit} --ar 9:16",
            "vo": "Most people think working 16-hour days or burning cash on broken methods is the answer. But it only leaves you exhausted.",
            "ost": "THE OLD WAY IS BROKEN ❌",
            "sfx": "Muffled ambient clock ticking with a subtle tension riser swell.",
            "match_cut": "Ending frame shows hero pausing and looking up as sudden realization strikes.",
            "transition": "Match cut on hero's upward gaze as warm sunrise light fills the loft (Scene 3)."
        },
        {
            "num": 3,
            "time": "0:20 - 0:30",
            "phase": "SCENE 3: THE BREAKTHROUGH & UNIQUE MECHANISM",
            "camera": "Smooth 360-degree orbital gimbal shot pulling back into a low-angle hero shot. 24mm wide anamorphic.",
            "lighting": "Warm golden hour sunlight breaking through the loft window, vibrant 5600K key light, cinematic bloom.",
            "prompt": f"Cinematic 4K hyper-detailed film shot, smooth 360 orbit around the SAME {hero_char} smiling with relief in {master_set} as {product_name} sleek holographic dashboard glows with golden aura, modern clean UI, photorealistic, shot on {camera_kit} --ar 9:16",
            "vo": f"That is why we built {product_name}. It attacks the root problem directly, giving you a proven step-by-step automated roadmap.",
            "ost": f"INTRODUCING: {product_name.upper()} ✅",
            "sfx": "Uplifting glockenspiel chime at 0:21 with full beat drop and driving groove.",
            "match_cut": "Ending frame shows hero standing up and turning right towards team area.",
            "transition": "Motion match pan following hero's walking motion to the lounge area (Scene 4)."
        },
        {
            "num": 4,
            "time": "0:30 - 0:40",
            "phase": "SCENE 4: THE TRANSFORMATION & REAL PROOF",
            "camera": "Dynamic side tracking dolly shot at 60fps slow-motion. 85mm portrait lens, buttery bokeh.",
            "lighting": "Bright, uplifting, high-key natural sunlight across the loft studio.",
            "prompt": f"Cinematic 4K slow motion 60fps film shot, side tracking dolly of the SAME {hero_char} holding a sleek tablet showing green upward revenue spike, high-fiving smiling colleague in {master_set}, genuine joy and confidence, shot on {camera_kit} --ar 9:16",
            "vo": f"Clients using {product_name} have transformed their numbers in record time—cutting stress in half while doubling their output.",
            "ost": "REAL RESULTS. ZERO GUESSWORK. 📈",
            "sfx": "Crisp cash register 'ka-ching' chime layered with triumphant synth melody.",
            "match_cut": "Ending frame shows hero placing tablet on table and gesturing to product bundle.",
            "transition": "Rack focus match cut onto the table surface (Scene 5)."
        },
        {
            "num": 5,
            "time": "0:40 - 0:50",
            "phase": "SCENE 5: THE GODFATHER VALUE STACK & GUARANTEE",
            "camera": "Rack focus from foreground 100% money-back guarantee gold seal to 3D product bonus stack beside hero. 50mm macro lens.",
            "lighting": "Pristine commercial studio product lighting in the loft, crisp metallic reflections.",
            "prompt": f"Hyper-detailed 3D cinematic film render of {product_name} complete toolkit bundle and bonus templates on the wooden desk in {master_set}, gold risk-free guarantee badge gleaming with light, the SAME {hero_char} standing proudly in background, shot on {camera_kit} --ar 9:16",
            "vo": "When you take action today, you get the entire system plus exclusive bonus templates—backed by our 100% money-back guarantee.",
            "ost": "FULL BUNDLE + 100% GUARANTEE 🛡️",
            "sfx": "Fast whoosh sound for each bonus reveal with confident voice accentuation.",
            "match_cut": "Ending frame shows hero stepping forward toward camera.",
            "transition": "Snap push to front eye-level MCU (Scene 6)."
        },
        {
            "num": 6,
            "time": "0:50 - 1:00",
            "phase": "SCENE 6: THE FINAL CALL TO ACTION (CTA) & URGENCY",
            "camera": "Front eye-level medium close-up (MCU) direct address with hand gesturing down to CTA button.",
            "lighting": "Clean, flattering warm commercial lighting, golden hour glow through windows.",
            "prompt": f"Cinematic 4K film shot, the SAME {hero_char} looking directly into camera with warm engaging smile in {master_set}, pointing downwards toward the bottom of the frame with urgency, shot on {camera_kit} --ar 9:16",
            "vo": "Click the link right below this video right now to claim your spot and download the blueprint before this promo ends!",
            "ost": "👇 TAP THE LINK BELOW TO START NOW",
            "sfx": "Climax musical resolution with a clear interface click / notification chime at 0:59.",
            "match_cut": "Final frame locks hero smiling and pointing down.",
            "transition": "Smooth 0.5s fade to branded logo end card with active URL link."
        }
    ]

    for i in range(min(num_scenes, len(scenes_data))):
        s = scenes_data[i]
        print(f"\n🎬 {s['phase']} [{s['time']}]")
        print(f"🎥 Camera & Optics: {s['camera']}")
        print(f"💡 Lighting & Tone: {s['lighting']}")
        print(f"🤖 AI Video Prompt (Google Veo / Sora / Kling / Runway):")
        print(f"   \"{s['prompt']}\"")
        print(f"🎙️ Spoken Voiceover (VO): \"{s['vo']}\"")
        print(f"📝 On-Screen Text (OST): {s['ost']}")
        print(f"🎵 Sound Design: {s['sfx']}")
        print(f"🎯 Match Cut Continuity: {s['match_cut']}")
        print(f"🔄 Transition to Next Scene: {s['transition']}")
        print("-" * 80)


def generate_blog_post(topic, target_audience, core_mistake, breakthrough_solution, hvco_name, cta_link):
    print("=" * 80)
    print("HIGH-CONVERTING THOUGHT-LEADERSHIP & SEO BLOG TEMPLATE")
    print("=" * 80)
    
    blog = f"""
# Why 90% of {target_audience} Fail at {topic} (And the 3-Step Fix)

If you're like most {target_audience}, you've probably spent countless hours trying to master {topic}.

You read the articles, watch the YouTube videos, and follow the standard advice. 
Yet despite all your effort, you're still running into the same frustrating roadblocks.

Why does this happen?

In this teardown, we're going to expose the fatal mistake most people make when approaching {topic}—and reveal the exact 3-step framework top performers use to achieve predictable results.

---

## The Fatal Mistake: {core_mistake}

Most advice in our industry focuses on vanity metrics rather than unit economics and direct response.

When you focus on {core_mistake}, two things happen:
1. You burn through your budget without acquiring predictable assets.
2. You attract low-intent prospects who drain your energy and haggle on price.

To fix this, you must invert your approach.

---

## The 3-Step Protocol for Dominating {topic}

### Step 1: Diagnose the 2:00 AM Nightmare
Never create content or offers in a vacuum. Deeply profile what keeps your ideal prospect awake at night.

### Step 2: Deploy {breakthrough_solution}
Instead of relying on outdated tactics, deploy a high-value mechanism that solves Problem A while establishing trust.

### Step 3: Stack Irresistible Value
Package your solution with sweetener bonuses, ironclad risk reversal, and clear scarcity.

---

## Ready to Master {topic}?

We've condensed this entire step-by-step system into an actionable, 15-page blueprint: **{hvco_name}**.

Inside, you'll discover:
- The exact swipe files and templates we use daily.
[ 👉 Click here to download your free copy of {hvco_name} now >> ]({cta_link})
"""
    print(blog)


def generate_google_ad(keyword, benefit, brand, target_url, pain):
    print("=" * 80)
    print("HIGH-INTENT GOOGLE SEARCH AD & EXTENSIONS (SABRI SUBY DIRECT-RESPONSE)")
    print("=" * 80)
    print(f"""
--- RESPONSIVE SEARCH AD (RSA) HEADLINES (≤ 30 Characters Each) ---
Headline 1 (Keyword Match):    Looking For {keyword[:17]}?
Headline 2 (Big Benefit):      {benefit[:30]}
Headline 3 (Brand Authority):  {brand[:20]} Official
Headline 4 (Pain Avoidance):   Stop Struggling with {pain[:9]}
Headline 5 (The Godfather Offer): 100% Free Blueprint Guide

--- DESCRIPTIONS (≤ 90 Characters Each) ---
Description 1: Tired of {pain}? Discover the battle-tested system to {benefit[:35]}. Download free.
Description 2: Rated 5 Stars by 400+ clients. 100% Money-Back Guarantee. Get instant access today!

--- SITELINK EXTENSIONS ---
• Sitelink 1: Free Strategy Roadmap (URL: {target_url}/roadmap)
  - Desc: Book a 1-on-1 audit with our team.
• Sitelink 2: Real Client Case Studies (URL: {target_url}/case-studies)
  - Desc: See how clients achieved 3x ROI.
• Sitelink 3: The Godfather Offer (URL: {target_url}/offer)
  - Desc: Explore our 100% risk-free package.

--- NEGATIVE KEYWORDS TO ADD IMMEDIATELY ---
free crack, torrent, pdf download free, jobs, salary, glassdoor, wiki, login, customer care number
""")


def generate_tiktok_ad(topic, avatar, pain, solution, cta_link):
    print("=" * 80)
    print("SHORT-FORM TIKTOK / REELS / SHORTS AD & HOOK VAULT")
    print("=" * 80)
    print(f"""
--- 5 HIGH-CONVERTING PATTERN-INTERRUPT HOOKS (0:00 - 0:03) ---
1. The Shocking Callout: "If you're a {avatar} still struggling with {pain}, stop scrolling right now."
2. The Contrarian Hook:  "Why 90% of what gurus teach about {topic} is a complete lie."
3. The Secret Expose:    "The #1 hidden reason why your {topic} isn't working (and nobody talks about this)."
4. The Story Hook:       "Two years ago, I almost lost everything because of {pain}..."
5. The 'Do Not Do This': "Please stop doing {pain} in 2026. Do this instead."

--- 30-SECOND FAST TIKTOK SCRIPT ---
[0:00-0:03] (Creator points at camera with shocked face)
"Stop scrolling if you're a {avatar}."

[0:03-0:12] (Cut to screen recording / stressed desk b-roll)
"Most people think solving {pain} requires working 16 hours a day. But that's backwards."

[0:12-0:22] (Creator holds up phone showing results)
"We deployed {solution}, and our results tripled in 21 days."

[0:22-0:30] (Finger points down to link button)
"I put the entire framework into a free 10-page guide. Tap the link in my bio or below to get it now!"

--- CAPTION & HASHTAGS ---
Tired of {pain}? Here is the exact framework to fix it in 2026 👇 Link in bio!
#marketingtips #{topic.replace(' ', '').lower()} #{avatar.replace(' ', '').lower()} #businessgrowth #directresponse
""")


def generate_seo_tags(source_url, source_lang, alt_langs, title, description):
    print("=" * 80)
    print("INTERNATIONAL SEO ASSET GENERATOR (HREFLANG, SITEMAP & JSON-LD SCHEMA)")
    print("=" * 80)
    
    langs = [l.strip() for l in alt_langs.split(",")]
    
    print("--- 1. HTML HREFLANG TAGS (Paste into <head>) ---")
    print(f'<link rel="alternate" hreflang="{source_lang}" href="{source_url}" />')
    for l in langs:
        print(f'<link rel="alternate" hreflang="{l}" href="{source_url.rstrip("/")}/{l}/" />')
    print(f'<link rel="alternate" hreflang="x-default" href="{source_url}" />\n')

    print("--- 2. HREFLANG XML SITEMAP FRAGMENT ---")
    print('<url>')
    print(f'  <loc>{source_url}</loc>')
    print(f'  <xhtml:link rel="alternate" hreflang="{source_lang}" href="{source_url}" />')
    for l in langs:
        print(f'  <xhtml:link rel="alternate" hreflang="{l}" href="{source_url.rstrip("/")}/{l}/" />')
    print('</url>\n')

    print("--- 3. LOCALIZED JSON-LD SCHEMA ---")
    schema = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{title}",
  "description": "{description}",
  "inLanguage": "{source_lang}",
  "url": "{source_url}"
}}
</script>'''
    print(schema)


def generate_email_sequence(avatar, goal, problem, product_name, price, guarantee_days, link_url):
    print("=" * 80)
    print("THE 4-PHASE EMAIL MACHINE SWIPE SUITE")
    print("=" * 80)
    
    suite = f"""
EMAIL 1 (DAY 0 - WELCOME & HVCO ASSET DELIVERY)
Send Time: Immediately on Opt-In
Subject: [Download] Here is your {product_name} Blueprint
Body:
Hey [First Name],

Here is the direct link to download the {product_name} Blueprint you requested:

>> Download Your Blueprint Here: {link_url}

Inside, you'll discover how to overcome {problem} and achieve {goal} without the usual headaches.

Whitelist my email so you don't miss our upcoming case study teardown.

Best,
[Your Name]

--------------------------------------------------------------------------------
EMAIL 2 (DAY 3 - MAGIC LANTERN STORY & LESSON)
Send Time: Tuesday at 10:00 AM Local Time
Subject: the $50k mistake...
Body:
Hey [First Name],

A few years ago, I made a mistake that almost cost me everything.

I thought solving {problem} was all about working harder.
I was grinding 14 hours a day, burning through cash, and getting nowhere.

That's when I discovered what I now call the "Value Inversion Principle".

Instead of competing with everyone else, we built {product_name}.
Within 30 days, we reached {goal} with complete predictability.

I recorded a short 10-minute teardown video showing how you can apply this:
>> Watch the 10-minute training here: {link_url}

Best,
[Your Name]

--------------------------------------------------------------------------------
EMAIL 3 (DAY 7 - THE GODFATHER OFFER PITCH)
Send Time: Thursday at 2:00 PM Local Time
Subject: private invitation for {avatar}?
Body:
Hey [First Name],

If you're serious about reaching {goal} without dealing with {problem}, doing it alone will cost you months of trial and error.

This week, we are opening 5 private spots for our {product_name} Accelerator.

You get:
✓ The Complete System (${price} Value)
✓ Fast-Action Template Vault (Free Bonus)
✓ Our {guarantee_days}-Day 100% Money-Back Guarantee

>> Claim one of the 5 spots here: {link_url}

Best,
[Your Name]

--------------------------------------------------------------------------------
EMAIL 4 (DAY 14 - THE FAMOUS 9-WORD COLD LEAD REVIVAL)
Send Time: Sunday at 8:30 PM Local Time
Subject: [First Name]
Body:
Hey [First Name],

Are you still looking for help with {goal}?

Best,
[Your Name]
"""
    print(suite)


def calculate_hormozi_value(dream_outcome_score, certainty_score, time_delay_score, effort_score):
    """
    Scores from 1 to 10.
    Value = (Dream Outcome * Perceived Likelihood) / (Time Delay * Effort)
    """
    numerator = dream_outcome_score * certainty_score
    denominator = max(0.1, (time_delay_score * effort_score) / 10.0)
    score = numerator / denominator
    print("=" * 80)
    print("ALEX HORMOZI VALUE EQUATION SCORE")
    print("=" * 80)
    print(f"• Dream Outcome (1-10): {dream_outcome_score}")
    print(f"• Perceived Likelihood of Achievement (1-10): {certainty_score}")
    print(f"• Time Delay (1-10, lower is faster): {time_delay_score}")
    print(f"• Effort & Sacrifice (1-10, lower is easier): {effort_score}")
    print(f"\n=> GRAND SLAM OFFER SCORE: {score:.1f} / 100")
    if score >= 50:
        print("🌟 STATUS: GRAND SLAM OFFER! High pricing power and extreme perceived value.")
    elif score >= 25:
        print("⚠️ STATUS: SOLID OFFER. To increase pricing power, decrease time delay and customer effort.")
    else:
        print("❌ STATUS: COMMODITY TRAP. Your offer requires too much effort or takes too long to deliver results.")


def generate_nigerian_whatsapp_scripts(product_name, price_ngn, promo_price_ngn, bonus_item):
    print("=" * 80)
    print("AKIN ALABI & MOFE RICHARD NIGERIAN WHATSAPP CONVERSION SUITE")
    print("=" * 80)
    
    script = f"""
1. THE 4-PART DAILY WHATSAPP STATUS FLOW:
------------------------------------------
Slide 1 (8:00 AM): "Good morning friends! Remember: Action cures fear. What is that one business goal you are attacking today?"
Slide 2 (1:00 PM): "Did you know why 85% of people fail to get original {product_name} in Nigeria? Most vendors sell refurbished grade-C. Here is how to test the real one in 3 seconds..."
Slide 3 (6:00 PM): [Post Screenshot of ₦{promo_price_ngn:,} bank transfer / Happy customer WhatsApp review from Lagos or Abuja] "Another delivery dispatched to Lekki Phase 1! Thank you for the trust 🙏"
Slide 4 (8:30 PM): "Flash Promo! We have only 4 units of {product_name} left in our Lagos store. Regular price is ₦{price_ngn:,}, but tonight you get it for ₦{promo_price_ngn:,} + FREE {bonus_item} + FREE Nationwide Delivery! Reply 'I WANT' now."

2. THE 1-ON-1 DM CLOSING SCRIPT (WHEN CUSTOMER ASKS 'HOW MUCH?'):
-----------------------------------------------------------------
You: "Hello Chief! Thanks for reaching out about our {product_name}. 
Before I give you the promo price, are you buying this for personal use or for your business?"

Customer: "For personal use."

You: (Send warm 20s voice note or text):
"Awesome! You made the right choice. With our original version, you never have to worry about fake quality or breakdowns.
The full package normally sells for ₦{price_ngn:,}. 
However, for our weekend special, you pay only ₦{promo_price_ngn:,}.
And to make it completely risk-free for you:
1. Nationwide Delivery is 100% FREE.
2. You get a FREE {bonus_item} worth ₦12,000.
3. You get our 30-Day Money-Back Guarantee!

Would you prefer morning or afternoon delivery to your address?"

3. PAYMENT ON DELIVERY (POD) CONFIRMATION PROTOCOL:
---------------------------------------------------
"To confirm your dispatch rider for tomorrow, please reply with:
1. Full Name:
2. Exact Delivery Address & Landmark:
3. Two Active Phone Numbers:
4. Preferred Delivery Time:

Note: Please ensure your cash or bank transfer of ₦{promo_price_ngn:,} is ready so the rider does not wait. Thank you!"
"""
    print(script)


def main():
    parser = argparse.ArgumentParser(description="Marketing Mastery Command Line Toolkit")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 1. Sales letter command
    sl_parser = subparsers.add_parser("sales-letter", help="Generate a 17-Step Sabri Suby Sales Letter")
    sl_parser.add_argument("--avatar", default="Business Owners", help="Target Avatar")
    sl_parser.add_argument("--outcome", default="Double Inbound Leads", help="Dream Outcome")
    sl_parser.add_argument("--timeframe", default="30 Days", help="Timeframe")
    sl_parser.add_argument("--obstacle", default="Burning Cash on Ads", help="Biggest Obstacle")
    sl_parser.add_argument("--mechanism", default="The Client Engine Protocol", help="Unique Mechanism")
    sl_parser.add_argument("--price", default="297", help="Selling Price")
    sl_parser.add_argument("--anchor", default="2,997", help="Anchor Total Value")
    sl_parser.add_argument("--guarantee", default="30", help="Guarantee Days")

    # 2. Meta ad command
    ad_parser = subparsers.add_parser("ad-copy", help="Generate Power 4 Meta Ad Copy")
    ad_parser.add_argument("--avatar", default="Coaches & Consultants", help="Target Avatar")
    ad_parser.add_argument("--pain", default="Inconsistent Monthly Revenue", help="Core Pain")
    ad_parser.add_argument("--solution", default="The Client Acquisition Playbook", help="HVCO / Solution")
    ad_parser.add_argument("--outcome", default="Add $20k/mo to Your Pipeline", help="Dream Outcome")
    ad_parser.add_argument("--link", default="https://example.com/free-blueprint", help="CTA Link URL")

    # 3. Story ad command
    sad_parser = subparsers.add_parser("story-ad", help="Generate Long-Form Narrative Story Ad")
    sad_parser.add_argument("--character", default="David", help="Main Character Name")
    sad_parser.add_argument("--obstacle", default="wasting $4,000/mo on useless marketing agencies", help="Core Obstacle")
    sad_parser.add_argument("--discovery", default="we tested Sabri Suby's 17-Step Secret Selling System", help="Discovery Moment")
    sad_parser.add_argument("--transformation", default="Client acquisition costs dropped by 64% in 30 days", help="Measurable Result")
    sad_parser.add_argument("--lesson", default="Never compete on price; build an irresistible Godfather Offer.", help="Universal Lesson")
    sad_parser.add_argument("--link", default="https://example.com/case-study", help="CTA Link URL")

    # 4. Story refinement command
    sr_parser = subparsers.add_parser("story-refine", help="Refine User Story using Paul Smith 8-Part Story Spine")
    sr_parser.add_argument("--story", default="I started my agency in 2020 and struggled for 2 years with no clients until I figured out cold email and scaled to 10k.", help="Raw Story Text")
    sr_parser.add_argument("--hero", default="Alex", help="Hero Name")
    sr_parser.add_argument("--lesson", default="Outbound without a Grand Slam Offer is wasted energy.", help="Business Lesson")
    sr_parser.add_argument("--cta", default="https://example.com/masterclass", help="Call to Action Link")

    # 5. Video ad command
    vid_parser = subparsers.add_parser("video-ad", help="Generate 60-90s Direct-Response Video Ad Script")
    vid_parser.add_argument("--hook", default="Stop scrolling if you want more clients", help="Opening Hook")
    vid_parser.add_argument("--pain", default="wasting money on Facebook Ads", help="Core Pain Point")
    vid_parser.add_argument("--solution", default="The 8-Phase Client Engine", help="Unique Mechanism Name")
    vid_parser.add_argument("--proof", default="Generated $1.33B in 416 Niches", help="Proof Metric")
    vid_parser.add_argument("--cta", default="Claim your free 15-page blueprint now", help="CTA Command")

    # 6. Blog post command
    blog_parser = subparsers.add_parser("blog-post", help="Generate High-Converting Thought-Leadership Blog Post")
    blog_parser.add_argument("--topic", default="B2B Client Acquisition", help="Core Topic")
    blog_parser.add_argument("--audience", default="SaaS Founders", help="Target Audience")
    blog_parser.add_argument("--mistake", default="relying on brand awareness instead of direct response", help="Core Mistake")
    blog_parser.add_argument("--solution", default="The Godfather Offer Protocol", help="Breakthrough Solution")
    blog_parser.add_argument("--hvco", default="The SaaS Growth Cheatsheet", help="HVCO Lead Magnet Title")
    blog_parser.add_argument("--link", default="https://example.com/saas-guide", help="CTA Link URL")

    # 7. Email sequence command
    em_parser = subparsers.add_parser("email-sequence", help="Generate 4-Phase Email Machine Suite")
    em_parser.add_argument("--avatar", default="Course Creators", help="Target Avatar")
    em_parser.add_argument("--goal", default="Sell Out Your Next Cohort", help="Dream Goal")
    em_parser.add_argument("--problem", default="Low Webinar Attendance", help="Core Problem")
    em_parser.add_argument("--product", default="The Cohort Accelerator", help="Product Name")
    em_parser.add_argument("--price", default="497", help="Product Price")
    em_parser.add_argument("--guarantee", default="30", help="Guarantee Days")
    em_parser.add_argument("--link", default="https://example.com/cohort", help="Offer Link URL")

def generate_dub_plan(video_url, to_lang, duration_seconds, bilingual, no_lipsync):
    print("=" * 80)
    print("PIKA LANGUAGE-SWAP VIDEO DUBBING & LOCALIZATION PLAN")
    print("=" * 80)

    lipsync_active = not no_lipsync and duration_seconds <= 300
    est_cost = (duration_seconds / 60.0) * 4.0 if lipsync_active else 0.0

    print(f"• Source Video URL: {video_url}")
    print(f"• Target Language: {to_lang}")
    print(f"• Video Duration: {duration_seconds} seconds")
    print(f"• Lipsync Active: {'YES (Est. cost: $' + f'{est_cost:.2f} at $4/min)' if lipsync_active else 'NO'}")
    print(f"• Subtitle Mode: {'Bilingual (Original + Translated Stacked)' if bilingual else 'Target Language Only'}")
    print("-" * 80)
    print("PIPELINE EXECUTION STEPS:")
    print("1. STEP 1: DUB VIDEO")
    print(f'   dub_video(source_video_url="{video_url}", target_language="{to_lang}", source_language="auto")')
    
    if lipsync_active:
        print("\n2. STEP 2: LIPSYNC (Re-match mouth to translated speech)")
        print('   edit_lipsync(video_url=<dubbed_video_url>)')
        caption_target = "<lipsynced_video_url>"
    else:
        print("\n2. STEP 2: LIPSYNC SKIPPED")
        caption_target = "<dubbed_video_url>"

    print("\n3. STEP 3: BURN CAPTIONS")
    if bilingual:
        print(f'   add_captions(video_url="{caption_target}", caption_mode="manual", subtitles=<dub_subtitles>, secondary_subtitles=<source_subtitles>, language="{to_lang}", secondary_subtitles_position="below", style="branded-space-mono", position="bottom")')
    else:
        print(f'   add_captions(video_url="{caption_target}", caption_mode="manual", subtitles=<dub_subtitles>, language="{to_lang}", style="branded-space-mono", position="bottom")')
    print("=" * 80)


def generate_localized_copy(language, avatar, pain, solution, dream_outcome, link_url):
    print("=" * 80)
    print(f"LOCALIZED DIRECT-RESPONSE AD COPY ({language.upper()})")
    print("=" * 80)

    if language.lower() in ["pidgin", "pcm", "nigerian-pidgin"]:
        ad = f"""
[HOOK / HEADLINE]
Attention all {avatar}: You don tire to dey suffer from {pain}? Abeg pause make you read this.

[THE LEAD]
Most people inside this business dey do everything backward.
Dem dey work 16 hours every day, dey waste money for things wey no dey work, but still dey broke and frustrated.

[THE STORY & SOLUTION]
Before before, I think say to achieve {dream_outcome}, person must kill himself with hard work.
Until I discover the secret: Na direct-response system dey bring real customers, no be luck!

Na why we create {solution}.
E dey give you step-by-step roadmap to get {dream_outcome} without any headache or story.

[CALL TO ACTION]
We don pack the whole secret inside one free guide.

Click the link below make you download your own copy 100% FREE before promo finish:

👉 Tap here to download now: {link_url}
"""
    elif language.lower() in ["es", "spanish", "español"]:
        ad = f"""
[HOOK / HEADLINE]
Atención {avatar}: ¿Cansado de luchar contra {pain}? Deja de hacer scroll ahora mismo.

[THE LEAD]
La mayoría en nuestra industria lo está haciendo todo al revés.
Trabajan 14 horas al día, prueban mil trucos diferentes y terminan agotados y sin resultados.

[THE STORY & SOLUTION]
Yo solía pensar que la única forma de lograr {dream_outcome} era sacrificar todo mi tiempo libre.
Hasta que descubrí el secreto: No se trata de esperar suerte, sino de tener un sistema predecible.

Por eso creamos {solution}.
Te da un plan paso a paso para alcanzar {dream_outcome} con total seguridad.

[CALL TO ACTION]
Hemos documentado todo el sistema en una guía gratuita.

Descarga tu copia 100% gratis antes de que expire esta promoción:

👉 Toca aquí para descargar ahora: {link_url}
"""
    elif language.lower() in ["fr", "french", "français"]:
        ad = f"""
[HOOK / HEADLINE]
Attention {avatar} : Vous en avez assez de lutter avec {pain} ? Arrêtez de scroller.

[THE LEAD]
La plupart des gens dans notre domaine font tout à l'envers.
Ils travaillent 14 heures par jour et finissent épuisés et frustrés.

[THE STORY & SOLUTION]
Nous avons conçu {solution} pour transformer votre approche et atteindre {dream_outcome} sans le stress habituel.

[CALL TO ACTION]
Téléchargez votre guide 100% gratuit dès maintenant :

👉 Cliquez ici pour y accéder : {link_url}
"""
    else:
        ad = f"""
[HOOK / HEADLINE ({language.upper()})]
Attention {avatar}: Overcome {pain} with {solution} to achieve {dream_outcome}.

[CALL TO ACTION]
Download your localized blueprint 100% Free:
👉 {link_url}
"""
    print(ad)


def main():
    parser = argparse.ArgumentParser(description="Marketing Mastery Command Line Toolkit")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 1. Sales letter command
    sl_parser = subparsers.add_parser("sales-letter", help="Generate a 17-Step Sabri Suby Sales Letter")
    sl_parser.add_argument("--avatar", default="Business Owners", help="Target Avatar")
    sl_parser.add_argument("--outcome", default="Double Inbound Leads", help="Dream Outcome")
    sl_parser.add_argument("--timeframe", default="30 Days", help="Timeframe")
    sl_parser.add_argument("--obstacle", default="Burning Cash on Ads", help="Biggest Obstacle")
    sl_parser.add_argument("--mechanism", default="The Client Engine Protocol", help="Unique Mechanism")
    sl_parser.add_argument("--price", default="297", help="Selling Price")
    sl_parser.add_argument("--anchor", default="2,997", help="Anchor Total Value")
    sl_parser.add_argument("--guarantee", default="30", help="Guarantee Days")
    sl_parser.add_argument("--lang", default="en", help="Language code (en, es, pcm, fr)")

    # 2. Meta ad command
    ad_parser = subparsers.add_parser("ad-copy", help="Generate Power 4 Meta Ad Copy")
    ad_parser.add_argument("--avatar", default="Coaches & Consultants", help="Target Avatar")
    ad_parser.add_argument("--pain", default="Inconsistent Monthly Revenue", help="Core Pain")
    ad_parser.add_argument("--solution", default="The Client Acquisition Playbook", help="HVCO / Solution")
    ad_parser.add_argument("--outcome", default="Add $20k/mo to Your Pipeline", help="Dream Outcome")
    ad_parser.add_argument("--link", default="https://example.com/free-blueprint", help="CTA Link URL")

    # 3. Story ad command
    sad_parser = subparsers.add_parser("story-ad", help="Generate Long-Form Narrative Story Ad")
    sad_parser.add_argument("--character", default="David", help="Main Character Name")
    sad_parser.add_argument("--obstacle", default="wasting $4,000/mo on useless marketing agencies", help="Core Obstacle")
    sad_parser.add_argument("--discovery", default="we tested Sabri Suby's 17-Step Secret Selling System", help="Discovery Moment")
    sad_parser.add_argument("--transformation", default="Client acquisition costs dropped by 64% in 30 days", help="Measurable Result")
    sad_parser.add_argument("--lesson", default="Never compete on price; build an irresistible Godfather Offer.", help="Universal Lesson")
    sad_parser.add_argument("--link", default="https://example.com/case-study", help="CTA Link URL")

    # 4. Story refinement command
    sr_parser = subparsers.add_parser("story-refine", help="Refine User Story using Paul Smith 8-Part Story Spine")
    sr_parser.add_argument("--story", default="I started my agency in 2020 and struggled for 2 years with no clients until I figured out cold email and scaled to 10k.", help="Raw Story Text")
    sr_parser.add_argument("--hero", default="Alex", help="Hero Name")
    sr_parser.add_argument("--lesson", default="Outbound without a Grand Slam Offer is wasted energy.", help="Business Lesson")
    sr_parser.add_argument("--cta", default="https://example.com/masterclass", help="Call to Action Link")

    # 5. Video ad command
    vid_parser = subparsers.add_parser("video-ad", help="Generate 60-90s Direct-Response Video Ad Script")
    vid_parser.add_argument("--hook", default="Stop scrolling if you want more clients", help="Opening Hook")
    vid_parser.add_argument("--pain", default="wasting money on Facebook Ads", help="Core Pain Point")
    vid_parser.add_argument("--solution", default="The 8-Phase Client Engine", help="Unique Mechanism Name")
    vid_parser.add_argument("--proof", default="Generated $1.33B in 416 Niches", help="Proof Metric")
    vid_parser.add_argument("--cta", default="Claim your free 15-page blueprint now", help="CTA Command")

    # 6. Blog post command
    blog_parser = subparsers.add_parser("blog-post", help="Generate High-Converting Thought-Leadership Blog Post")
    blog_parser.add_argument("--topic", default="B2B Client Acquisition", help="Core Topic")
    blog_parser.add_argument("--audience", default="SaaS Founders", help="Target Audience")
    blog_parser.add_argument("--mistake", default="relying on brand awareness instead of direct response", help="Core Mistake")
    blog_parser.add_argument("--solution", default="The Godfather Offer Protocol", help="Breakthrough Solution")
    blog_parser.add_argument("--hvco", default="The SaaS Growth Cheatsheet", help="HVCO Lead Magnet Title")
    blog_parser.add_argument("--link", default="https://example.com/saas-guide", help="CTA Link URL")

    # 7. Email sequence command
    em_parser = subparsers.add_parser("email-sequence", help="Generate 4-Phase Email Machine Suite")
    em_parser.add_argument("--avatar", default="Course Creators", help="Target Avatar")
    em_parser.add_argument("--goal", default="Sell Out Your Next Cohort", help="Dream Goal")
    em_parser.add_argument("--problem", default="Low Webinar Attendance", help="Core Problem")
    em_parser.add_argument("--product", default="The Cohort Accelerator", help="Product Name")
    em_parser.add_argument("--price", default="497", help="Product Price")
    em_parser.add_argument("--guarantee", default="30", help="Guarantee Days")
    em_parser.add_argument("--link", default="https://example.com/cohort", help="Offer Link URL")

    # 8. Value equation command
    val_parser = subparsers.add_parser("score-offer", help="Score Offer via Alex Hormozi Value Equation")
    val_parser.add_argument("--dream", type=float, default=9.0, help="Dream Outcome Score (1-10)")
    val_parser.add_argument("--certainty", type=float, default=8.5, help="Perceived Likelihood Score (1-10)")
    val_parser.add_argument("--time-delay", type=float, default=2.0, help="Time Delay Score (1-10, lower is better)")
    val_parser.add_argument("--effort", type=float, default=2.5, help="Effort & Sacrifice Score (1-10, lower is better)")

    # 9. Nigerian WhatsApp command
    ng_parser = subparsers.add_parser("nigeria-whatsapp", help="Generate Nigerian WhatsApp Selling Scripts")
    ng_parser.add_argument("--product", default="Smart Solar Power Station", help="Product Name")
    ng_parser.add_argument("--price", type=int, default=150000, help="Original Price in NGN")
    ng_parser.add_argument("--promo", type=int, default=95000, help="Promo Price in NGN")
    ng_parser.add_argument("--bonus", default="Fast-Charge Cable Kit + LED Lamp", help="Free Bonus Gift")

    # 10. Video Dubbing & Language Swap Plan command
    dub_parser = subparsers.add_parser("dub-plan", help="Generate Video Dubbing & Language Swap Plan")
    dub_parser.add_argument("--video-url", default="https://example.com/video.mp4", help="Public HTTPS Video URL")
    dub_parser.add_argument("--to-lang", default="es", help="Target Language Code (e.g. es, fr, de, ja, zh, pcm)")
    dub_parser.add_argument("--duration", type=int, default=45, help="Video Duration in Seconds")
    dub_parser.add_argument("--bilingual", action="store_true", help="Burn Bilingual Subtitles")
    dub_parser.add_argument("--no-lipsync", action="store_true", help="Skip Lipsync Step")

    # 12. Google Ad command
    goog_parser = subparsers.add_parser("google-ad", help="Generate High-Intent Google Search RSA Ads & Extensions")
    goog_parser.add_argument("--keyword", default="Client Acquisition System", help="Target Search Keyword")
    goog_parser.add_argument("--benefit", default="Double Inbound Leads in 30 Days", help="Big Promise Benefit")
    goog_parser.add_argument("--brand", default="ClientEngine", help="Brand Name")
    goog_parser.add_argument("--url", default="https://example.com", help="Target Landing Page URL")
    goog_parser.add_argument("--pain", default="wasting money on low ROI ads", help="Core Customer Pain")

    # 13. TikTok / Reels Ad command
    tik_parser = subparsers.add_parser("tiktok-ad", help="Generate Short-Form TikTok/Reels Hooks & 30s Scripts")
    tik_parser.add_argument("--topic", default="Agency Growth", help="Topic Name")
    tik_parser.add_argument("--avatar", default="Agency Owner", help="Target Avatar")
    tik_parser.add_argument("--pain", default="working 16-hour days with zero profit", help="Core Pain")
    tik_parser.add_argument("--solution", default="The Automated Client Machine", help="Solution Name")
    tik_parser.add_argument("--link", default="https://example.com/bio-link", help="CTA Link")

    # 14. SEO & Hreflang Tags command
    seo_parser = subparsers.add_parser("seo-tags", help="Generate International Hreflang Tags, Sitemap & JSON-LD Schema")
    seo_parser.add_argument("--url", default="https://example.com/blog/scaling-guide", help="Source Article URL")
    seo_parser.add_argument("--source-lang", default="en", help="Source Language Code")
    seo_parser.add_argument("--alt-langs", default="es,fr,de,pt-BR", help="Comma-separated Target Language Codes")
    seo_parser.add_argument("--title", default="How to Scale Your Agency in 2026", help="Article Headline")
    seo_parser.add_argument("--desc", default="Discover the step-by-step framework to scale client acquisition.", help="Meta Description")

    # 15. AI Video Scene Creator command
    ai_vid_parser = subparsers.add_parser("ai-video", help="Generate Hollywood-Grade 10-Second Scene Prompts & Scripts for AI Video Tools")
    ai_vid_parser.add_argument("--product", default="The 7-Figure Client Engine", help="Product / Service Name")
    ai_vid_parser.add_argument("--audience", default="B2B Agency Owners", help="Target Audience / Avatar")
    ai_vid_parser.add_argument("--duration", type=int, default=60, help="Total Video Duration in Seconds (e.g. 30, 60, 90)")
    ai_vid_parser.add_argument("--more-info", default="Free 15-page blueprint download + 30-day risk-free guarantee", help="Special Offer / Pricing / Key Features")

    args = parser.parse_args()

    if args.command == "sales-letter":
        generate_17_step_sales_letter(args.avatar, args.outcome, args.timeframe, args.obstacle, args.mechanism, args.price, args.anchor, args.guarantee, args.lang)
    elif args.command == "ad-copy":
        generate_power_4_ad(args.avatar, args.pain, args.solution, args.outcome, args.link)
    elif args.command == "story-ad":
        generate_story_ad(args.character, args.obstacle, args.discovery, args.transformation, args.lesson, args.link)
    elif args.command == "story-refine":
        generate_story_ad_from_refine = refine_user_story(args.story, args.hero, args.lesson, args.cta)
    elif args.command == "video-ad":
        generate_video_ad_script(args.hook, args.pain, args.solution, args.proof, args.cta)
    elif args.command == "blog-post":
        generate_blog_post(args.topic, args.audience, args.mistake, args.solution, args.hvco, args.link)
    elif args.command == "email-sequence":
        generate_email_sequence(args.avatar, args.goal, args.problem, args.product, args.price, args.guarantee, args.link)
    elif args.command == "score-offer":
        calculate_hormozi_value(args.dream, args.certainty, args.time_delay, args.effort)
    elif args.command == "nigeria-whatsapp":
        generate_nigerian_whatsapp_scripts(args.product, args.price, args.promo, args.bonus)
    elif args.command == "dub-plan":
        generate_dub_plan(args.video_url, args.to_lang, args.duration, args.bilingual, args.no_lipsync)
    elif args.command == "translate-copy":
        generate_localized_copy(args.lang, args.avatar, args.pain, args.solution, args.outcome, args.link)
    elif args.command == "google-ad":
        generate_google_ad(args.keyword, args.benefit, args.brand, args.url, args.pain)
    elif args.command == "tiktok-ad":
        generate_tiktok_ad(args.topic, args.avatar, args.pain, args.solution, args.link)
    elif args.command == "seo-tags":
        generate_seo_tags(args.url, args.source_lang, args.alt_langs, args.title, args.desc)
    elif args.command == "ai-video":
        generate_ai_video_director_scenes(args.product, args.audience, args.duration, args.more_info)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


