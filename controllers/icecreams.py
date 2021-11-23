from werkzeug.exceptions import BadRequest

facts = [
    {'id': 1, 'fact': 'One of the most unusual ice cream flavors is hot dog flavored ice-cream that was created in Arizona, US.'},
    {'id': 2, 'fact': 'End of the World War II was celebrated by eating ice cream'},
    {'id': 3, 'fact': 'Ice cream was first invented in seventh-century China, where King Tang of Shang had a group of “ice men” create a cold dessert made from buffalo milk, flour, and camphor'}
]

def index(req):
    return [f for f in facts], 200

def show(req, uid):
    return find_by_uid(uid), 200

def create(req):
    new_fact = req.get_json()
    new_fact['id'] = sorted([f['id'] for f in facts])[-1] + 1
    facts.append(new_fact)
    return new_fact, 201

def destroy(req, uid):
    fact = find_by_uid(uid)
    facts.remove(fact)
    return fact, 204

def find_by_uid(uid):
    try:
        return next(fact for fact in facts if fact['id'] == uid)
    except:
        raise BadRequest(f'There is no fact with id {uid}')