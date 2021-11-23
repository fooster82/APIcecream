import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'Hello from APIcecream!'

    def test_get_factss(self, api):
        res = api.get('/icecream/facts')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_get_fact(self, api):
        res = api.get('/icecream/facts/2')
        assert res.status == '200 OK'
        assert res.json['fact'] == 'Test Fact 2'

    def test_get_facts_error(self, api):
        res = api.get('/icecream/facts/4')
        assert res.status == '400 BAD REQUEST'
        assert "fact with id 4" in res.json['message']

    def test_post_facts(self, api):
        mock_data = json.dumps({'fact': 'Ice cream is nice'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/icecream/facts', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 3

    def test_delete_fact(self, api):
        res = api.delete('/icecream/facts/1')
        assert res.status == '204 NO CONTENT'

    def test_not_found(self, api):
        res = api.get('/bob')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']