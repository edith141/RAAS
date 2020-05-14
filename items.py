from flask_restful import Resource, reqparse

class Zero(Resource):
    def get(self, name):
        return {'insult': f"Zero, that's the number of fucks I give, {name}"}

class AnywayCompany(Resource):
    def get(self, name):
        return {'insult': f"Who the fuck are you anyway, {name}, why are you stirring up so much trouble, and, who pays you?"}

class Awesome(Resource):
    def get(self):
        return {'insult': f"This is Fucking Awesome! I'd say that if I gave any shit about it."}
        
class Asshole(Resource):
    def get(self):
        return {'insult': f"Fuck you, asshole."}
        
class Backoff(Resource):
    def get(self, name):
        return {'insult': f"{name}, back the fuck off."}

class Bag(Resource):
    def get(self):
        return {'insult': f"Eat a bag of fucking dicks."}

class BallmerCompany(Resource):
    def get(self, company, name):
        return {'insult': f"Fucking {name} is a fucking pussy. I'm going to fucking bury that guy, I have done it before, and I will do it again. I'm going to fucking kill {company}."}

class Bday(Resource):
    def get(self, name):
        return {'insult': f"FHappy Fucking Birthday, {name}."}


class Why(Resource):
    def get(self):
        return {'insult': f"Why? Because fuck you, that's why."}
        

class Blackadder(Resource):
    def get(self, name):
        return {'insult': f"{name}, your head is as empty as a eunuch’s underpants. Fuck off!"}

class Bravo(Resource):
    def get(self, name):
        return {'insult': f"Bravo {name}, you just became a Scump!"}


class Bucket(Resource):
    def get(self):
        return {'insult': f"Please choke on a bucket of cocks."}

class Bus(Resource):
    def get(self, name):
        return {'insult': f"Christ on a bendy-bus, {name}, don't be such a fucking faff-arse"}

class Bye(Resource):
    def get(self):
        return {'insult': f"Fuckity bye already! "}

class CanIUse(Resource):
    def get(self, tool):
        return {'insult': f"Can you use {tool}? Fuck no!"}

class Chainsaw(Resource):
    def get(self, name):
        return {'insult': f"Fuck me gently with a chainsaw, {name}. Do I look like Mother Teresa?"}

class Worthless(Resource):
    def get(self, name):
        return {'insult': f"Fuck off {name}, you worthless cocksplat!"}

class Cool(Resource):
    def get(self):
        return {'insult': f"Cool story, bro."}

class Cup(Resource):
    def get(self):
        return {'insult': f"How about a nice cup of shut the fuck up?"}

class Hypocritical(Resource):
    def get(self, name):
        return {'insult': f"{name} you are being the usual slimy hypocritical asshole... You may have had value ten years ago, but people will see that you don't anymore."}

class Chat(Resource):
    def get(self):
        return {'insult': f"I'd love to stop and chat to you but I'd rather have type 2 diabetes."}

class Donut(Resource):
    def get(self, name):
        return {'insult': f"{name}, go and take a flying fuck at a rolling donut."}

class DoSomething(Resource):
    def get(self, do, something):
        return {'insult': f"{do} the fucking {something}!"}

class Equity(Resource):
    def get(self, name):
        return {'insult': f"Equity only? Long hours? Zero Pay? Well {name}, just sign me right the fuck up."}

class CantEven(Resource):
    def get(self, thing):
        return {'insult': f"I can't fuckin' even {thing}."}

class Everyone(Resource):
    def get(self):
        return {'insult': f"Everyone can go and fuck off."}

class Everything(Resource):
    def get(self):
        return {'insult': f"Fuck everything."}
        
class Family(Resource):
    def get(self):
        return {'insult': f"Fuck you, your whole family, your pets, and your feces."}
        
class Fascinating(Resource):
    def get(self, name):
        return {'insult': f"Fascinating story {name}, in what chapter do you shut the fuck up?"}

class Flying(Resource):
    def get(self):
        return {'insult': f"I don't give a flying fuck. "}

class Ftfy(Resource):
    def get(self):
        return {'insult': f"Fuck That, Fuck You!"}

class Fever(Resource):
    def get(self, name):
        return {'insult': f"Go fuck yourself {name}, you'll disappoint fewer people"}

class FTS(Resource):
    def get(self, name):
        return {'insult': f"Fuck that shit, {name}."}

class Holygrail(Resource):
    def get(self):
        return {'insult': f"I don't want to talk to you, no more, you empty-headed animal, food trough wiper. I fart in your general direction. Your mother was a hamster and your father smelt of elderberries. Now go away or I shall taunt you a second time."}

class Horse(Resource):
    def get(self, name):
        return {'insult': f"Fuck you and the horse you rode in on, {name}"}

class Immensity(Resource):
    def get(self):
        return {'insult': f"You can not imagine the immensity of the FUCK I do not give."}

class Keep(Resource):
    def get(self, name):
        return {'insult': f"{name}, Fuck off. And when you get there, fuck off from there too. Then fuck off some more. Keep fucking off until you get back here. Then fuck off again."}

class Calm(Resource):
    def get(self, reaction):
        return {'insult': f"Keep the fuck calm and {reaction}!"}

class King(Resource):
    def get(self, name):
        return {'insult': f"Oh fuck off, just really fuck off you total dickface. Good God, {name}, you are fucking thick."}

class Foreign(Resource):
    def get(self, name):
        return {'insult': f"{name}, there aren't enough swear-words in the English language, so now I'll have to call you perkeleen vittupää just to express my disgust and frustration with this crap. "}

class Look(Resource):
    def get(self, name):
        return {'insult': f"{name}, do I look like I give a fuck?"}

class Looking(Resource):
    def get(self):
        return {'insult': f"Looking for a fuck to give. "}

class Insane(Resource):
    def get(self, name):
        return {'insult': f"What you've just said is one of the most insanely idiotic things I have ever heard, {name}. At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought. Everyone who heard that is now dumber for having listened to it. I award you no points {name}, and may God have mercy on your soul."}

class Maybe(Resource):
    def get(self):
        return {'insult': f"Maybe. Maybe not. Maybe fuck yourself. "}

class No(Resource):
    def get(self):
        return {'insult': f"No fucks given"}

class Nugget(Resource):
    def get(self, name):
        return {'insult': f"Well {name}, aren't you a shining example of a rancid fuck-nugget"}

class Outside(Resource):
    def get(self, name):
        return {'insult': f"{name}, why don't you go outside and play hide-and-go-fuck-yourself? "}

class Particular(Resource):
    def get(self, thing):
        return {'insult': f"Fuck this {thing} in particular."}

class Programmer(Resource):
    def get(self):
        return {'insult': f"Fuck you, I'm the programmer, bitch! "}

class Language(Resource):
    def get(self, lang):
        return {'insult': f"{lang}, motherfucker, do you speak it?"}

class Rat(Resource):
    def get(self):
        return {'insult': f"I don't give a rat's arse."}

class Shakespeare(Resource):
    def get(self, name):
        return {'insult': f"{name}, Thou clay-brained guts, thou knotty-pated fool, thou whoreson obscene greasy tallow-catch! "}

class Thumbs(Resource):
    def get(self):
        return {'insult': f"Who has two thumbs and doesn't give a fuck?"}

class Time(Resource):
    def get(self, name):
        return {'insult': f"I don't waste my fucking time with your bullshit {name}!"}
















