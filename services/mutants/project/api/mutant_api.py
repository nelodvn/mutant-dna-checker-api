from __future__ import division

from flask import Blueprint, jsonify, request
from project.api.mutant_checker import MutantChecker
from project import mongo

mutants_blueprint = Blueprint('mutants', __name__)


class MutantRequest():
    def __init__(self, dna, isMutant):
        self.dna = dna
        self.isMutant = isMutant

    def to_json(self):
        return {'dna': self.dna, 'isMutant': self.isMutant}


@mutants_blueprint.route('/mutant', methods=['POST'])
def check_mutant():
    post_data = request.get_json()
    dna = post_data.get('dna')
    try:
        checker = MutantChecker()
        isMutant = checker.isMutant(dna)
        req = MutantRequest(dna, isMutant)
        if not mongo.db.mutant.find_one(req.to_json()):
            mongo.db.mutant.insert(req.to_json())
        if isMutant:
            return jsonify({'isMutant': True}), 200
        else:
            return jsonify({'isMutant': False}), 403
    except ValueError as e:
        return jsonify({'error_message': str(e)}), 400


@mutants_blueprint.route('/stats', methods=['GET'])
def stats():
    mutants_count = mongo.db.mutant.find({'isMutant': True}).count()
    humans_count = mongo.db.mutant.find({'isMutant': False}).count()
    ratio = 0
    if mutants_count > 0 and humans_count > 0:
        ratio = mutants_count/humans_count
    return jsonify({'count_mutant_dna': mutants_count,
                    'count_human_dna': humans_count,
                    'ratio': ratio})
