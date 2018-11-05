import json

from project import create_app, mongo
from project.tests.base import BaseTestCase
from project.api.mutants import MutantRequest

app = create_app()


class TestMutantApi(BaseTestCase):

    def formatInputPayload(self, dna):
        return {'dna': dna}

    def test_check_valid_mutant(self):
        '''Ensures check mutant API service returns 200 (ok)
            for a valid mutant DNA payload'''

        with self.client:
            response = self.client.post('/mutant',
                                        data=json.dumps(self.formatInputPayload(self.valid_mutant_dna)),
                                        content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_check_invalid_mutant(self):
        '''Ensures check mutant service API returns 403 when the inputed DNA payload
            is not mutant (valid human DNA).'''
        with self.client:
            response = self.client.post('/mutant',
                                        data=json.dumps(self.formatInputPayload(self.valid_human_dna)),
                                        content_type='application/json')
            self.assertEqual(response.status_code, 403)

    def test_check_invalid_char_dna(self):
        '''Ensures check mutant service returns 400 when the inputed DNA is not valid
            (only acepts A, T, G, C).'''
        with self.client:
            response = self.client.post('/mutant',
                                        data=json.dumps(self.formatInputPayload(self.invalid_chars_dna)),
                                        content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_check_empty_input(self):
        '''Ensures the API returns a bad input when no DNA is informed'''
        with self.client:
            response = self.client.post('/mutant',
                                        content_type='application/json')
            self.assertEqual(response.status_code, 400)

            response = self.client.post('/mutant',
                                        data=json.dumps({'dna': ''}),
                                        content_type='application/json')
            self.assertEqual(response.status_code, 400)

    def test_stats(self):
        '''Ensure the API /stats is working.'''
        with self.client:
            response = self.client.get('/stats')
            data = json.loads(response.data.decode())
            self.assertEqual(data['count_human_dna'], 0)
            self.assertEqual(data['count_mutant_dna'], 0)
            self.assertEqual(data['ratio'], 0)

        mr = MutantRequest(self.valid_mutant_dna, True)
        mongo.db.mutant.insert(mr.to_json())

        with self.client:
            response = self.client.get('/stats')
            data = json.loads(response.data.decode())
            self.assertEqual(data['count_human_dna'], 0)
            self.assertEqual(data['count_mutant_dna'], 1)
            self.assertEqual(data['ratio'], 0)

        mr = MutantRequest(self.valid_human_dna, False)
        mongo.db.mutant.insert(mr.to_json())

        with self.client:
            response = self.client.get('/stats')
            data = json.loads(response.data.decode())
            self.assertEqual(data['count_human_dna'], 1)
            self.assertEqual(data['count_mutant_dna'], 1)
            self.assertEqual(data['ratio'], 1)


    def test_duplicated(self):
        '''Ensures the API does not insert duplicated registers to mongo DB.'''

        mr = MutantRequest(self.valid_mutant_dna, True)
        mongo.db.mutant.insert(mr.to_json())
        with self.client:
            response = self.client.post('/mutant',
                                         data=json.dumps(self.formatInputPayload(self.valid_mutant_dna)),
                                         content_type='application/json')

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, mongo.db.mutant.find(mr.to_json()).count(), 1)
