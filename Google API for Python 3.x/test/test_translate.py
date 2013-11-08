from apiclient.discovery import build
import sys
err = sys.stderr

def test_api():
    service = build('translate', 'v2', 
            developerKey='AIzaSyCP0aaTt8Rh6pTe8GmhpVPdZWFlq-diA7Y')
    sentence = "Le contenu du probable accord en cours de négociations n'a absolument pas filtré."
    translated_sentence_obj = service.translations().list(
            source='fr',
            target='en',
            q=[sentence]
            ).execute()
    translated_sentence = translated_sentence_obj['translations'][0]['translatedText']
    assert translated_sentence != sentence, "'%s' should not equal '%s'" % (translated_sentence, sentence)
    err.write("Translated sentence: '%s'\n" % translated_sentence)