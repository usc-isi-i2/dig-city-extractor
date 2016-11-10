import sys
import time
import os
import json
import codecs
import unittest

from digExtractor.extractor import Extractor
from digExtractor.extractor_processor import ExtractorProcessor
from digCountryPredictorExtractor.city_extractor import CityExtractor

class TestCityExtractorMethods(unittest.TestCase):

    def load_file(self, filename):
        names_file = os.path.join(os.path.dirname(__file__), filename)
        names = json.load(codecs.open(names_file, 'r', 'utf-8'))
        return names

    def test_city_extractor(self):
        doc = {'content': "\n \n \n \n \n \n \n ID#182730 - LegendaryDave - Salt Lake - Gay Escorts & Gay Massage \n \n \n \n \n \n \n \n \n LegendaryDave \n \n 2120.5 Miles Away \n \n \n \n \n \n \n THE LEGENDARY DAVE- 1ST TIME IN SALT LAKE CITY \n \n \n \n \n \n Over 200 Reviews! ***Voted one of the Top 50 Escorts in the USA, for the last 5 years in a row*** Secure, Masculine, Adventurous. Top/Vers Stud. Teacher to the New/Curious. Good-looking, Bi, Sense of Humor, Fun. Great Body. Educated, Honest, Sane. Healthy/DDF/Neg. AM,PM, 24/7, Overnights, Multi-Days. Very Skilled: Massage or Vanilla or Kink or Wild. Discreet & Professional. Incalls & Outcalls: USA & Abroad. VISIT MY WEBSITE FOR RATES, MORE HOT PICS, ALL MY REVIEWS, HIRING TIPS & MORE. \n \n \n \n \n his stats \n \n \n \n AGE:  45 \n Role:   Versatile \n HEIGHT:  5'11\" (180cm) \n WEIGHT:  150 - 170 lbs (68 - 77 kg) \n Piercings:  Not Specified \n \n \n RACE:  White \n HAIR COLOR:  Dark Brown \n EYE COLOR:  Green \n Open To  LTR :  Yes \n Languages:  English, Other \n \n \n BODY TYPE:  Muscular/Buff \n BODY HAIR:  Moderately hairy \n Tattoos:  Not Specified \n Smoker:  Not Specified \n \n \n \n \n \n \n reviews \n \n \r\n  M4RN Reviews:  8  Most Recent M4RN Star Review:  04/30/2016 \n \n \n \n \n \n \n \n \n \n services provided \n \n \n Escort  yes \n HOT Massage  yes \n Massage  yes \n Registered Therapist  yes \n In Calls  yes \n Out Calls  yes \n US Travel  yes \n Int'l Travel  yes \n Advertiser Since  Dec '07 \n \n \n \n \n \n contact info \n \n Phone: \n PREFERS PHONE CONTACT \n \n \n \n \n location  2120.5 Miles \n \n \n area:  Salt Lake City / Ogden \n Local City:  Salt Lake \n Postal Code:  84101 \n \n \n \n \n \n \n availability \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n s \n m \n t \n w \n t \n f \n s \n \n \n \n \n 7am-11am \n \n \n \n \n \n \n \n \n \n 11am-3pm \n \n \n \n \n \n \n \n \n \n 3pm-7pm \n \n \n \n \n \n \n \n \n \n 7pm-11pm \n \n \n \n \n \n \n \n \n \n 11pm-3am \n \n \n \n \n \n \n \n \n \n 3am-7am \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n Elite & Platinum Advertisers \n \n \n \n ELITE \n \n \n Toronto \n \n \n \n Barcelona \n \n \n \n San Francisco / Oakland \n \n \n \n Cleveland / Lorain / Elyria \n \n \n \n Los Angeles / West Hollywood \n \n \n \n \n \n \n Find LegendaryDave, Rent Men and Male Massage in Salt Lake \n \n \n \n \n \n \n \n \n \n \n \n \n"}
        cities = self.load_file("cities.json")
        stop_words = self.load_file("stop_words.json")
        extractor = CityExtractor().set_cities(cities).set_metadata({'extractor': 'city'}).set_stop_words(stop_words)
        extractor_processor = ExtractorProcessor().set_input_fields(['content']).set_output_field('cities').set_extractor(extractor)
        updated_doc = extractor_processor.extract(doc)
        self.assertEqual(updated_doc['cities'][0]['value'], list([u'orlando']))    

    def test_state_extractor(self):
        doc = {'content': "\n \n \n \n \n \n \n ID#182730 -  florida LegendaryDave - Salt Lake - Gay Escorts & Gay Massage \n \n \n \n \n \n \n \n \n LegendaryDave \n \n 2120.5 Miles Away \n \n \n \n \n \n \n THE LEGENDARY DAVE- 1ST TIME IN SALT LAKE CITY \n \n \n \n \n \n Over 200 Reviews! ***Voted one of the Top 50 Escorts in the USA, for the last 5 years in a row*** Secure, Masculine, Adventurous. Top/Vers Stud. Teacher to the New/Curious. Good-looking, Bi, Sense of Humor, Fun. Great Body. Educated, Honest, Sane. Healthy/DDF/Neg. AM,PM, 24/7, Overnights, Multi-Days. Very Skilled: Massage or Vanilla or Kink or Wild. Discreet & Professional. Incalls & Outcalls: USA & Abroad. VISIT MY WEBSITE FOR RATES, MORE HOT PICS, ALL MY REVIEWS, HIRING TIPS & MORE. \n \n \n \n \n his stats \n \n \n \n AGE:  45 \n Role:   Versatile \n HEIGHT:  5'11\" (180cm) \n WEIGHT:  150 - 170 lbs (68 - 77 kg) \n Piercings:  Not Specified \n \n \n RACE:  White \n HAIR COLOR:  Dark Brown \n EYE COLOR:  Green \n Open To  LTR :  Yes \n Languages:  English, Other \n \n \n BODY TYPE:  Muscular/Buff \n BODY HAIR:  Moderately hairy \n Tattoos:  Not Specified \n Smoker:  Not Specified \n \n \n \n \n \n \n reviews \n \n \r\n  M4RN Reviews:  8  Most Recent M4RN Star Review:  04/30/2016 \n \n \n \n \n \n \n \n \n \n services provided \n \n \n Escort  yes \n HOT Massage  yes \n Massage  yes \n Registered Therapist  yes \n In Calls  yes \n Out Calls  yes \n US Travel  yes \n Int'l Travel  yes \n Advertiser Since  Dec '07 \n \n \n \n \n \n contact info \n \n Phone: \n PREFERS PHONE CONTACT \n \n \n \n \n location  2120.5 Miles \n \n \n area:  Salt Lake City / Ogden \n Local City:  Salt Lake \n Postal Code:  84101 \n \n \n \n \n \n \n availability \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n s \n m \n t \n w \n t \n f \n s \n \n \n \n \n 7am-11am \n \n \n \n \n \n \n \n \n \n 11am-3pm \n \n \n \n \n \n \n \n \n \n 3pm-7pm \n \n \n \n \n \n \n \n \n \n 7pm-11pm \n \n \n \n \n \n \n \n \n \n 11pm-3am \n \n \n \n \n \n \n \n \n \n 3am-7am \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n Elite & Platinum Advertisers \n \n \n \n ELITE \n \n \n Toronto \n \n \n \n Barcelona \n \n \n \n San Francisco / Oakland \n \n \n \n Cleveland / Lorain / Elyria \n \n \n \n Los Angeles / West Hollywood \n \n \n \n \n \n \n Find LegendaryDave, Rent Men and Male Massage in Salt Lake \n \n \n \n \n \n \n \n \n \n \n \n \n"}
        states = self.load_file("states.json")
        stop_words = self.load_file("stop_words.json")
        extractor = CityExtractor().set_cities(states).set_metadata({'extractor': 'state'}).set_stop_words(stop_words)
        extractor_processor = ExtractorProcessor().set_input_fields(['content']).set_output_field('state').set_extractor(extractor)
        updated_doc = extractor_processor.extract(doc)
        self.assertEqual(updated_doc['state'][0]['value'], list([u'florida']))


if __name__ == '__main__':
    unittest.main()



