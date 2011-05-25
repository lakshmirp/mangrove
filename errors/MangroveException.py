# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
#TODO: Please Read Readme.rst of errors before defining any new exception


class MangroveException(Exception):
    def __init__(self, message, data=None):
        self.message = message
        self.data = data

    def __str__(self):
        return self.message


class DataObjectAlreadyExists(MangroveException):
    def __init__(self, dataobject_name, param, value):
        error_message = "%s with %s = %s already exists." % (dataobject_name, param, value)
        MangroveException.__init__(self, error_message, (param, value))


class DataObjectNotFound(MangroveException):
    def __init__(self, dataobject_name, param, value):
        error_message = "%s with %s = %s not found." % (dataobject_name, param, value)
        MangroveException.__init__(self, error_message, (param, value))


class EntityTypeAlreadyDefined(MangroveException):
    pass


class FormModelDoesNotExistsException(MangroveException):
    def __init__(self, questionnaire_code):
        error_message = "The questionnaire with code %s does not exist." % questionnaire_code if questionnaire_code else "The questionnaire does not exist."
        MangroveException.__init__(self, error_message, (questionnaire_code, ))


class FieldDoesNotExistsException(MangroveException):
    def __init__(self, field_code):
        MangroveException.__init__(self, "The field with code %s does not exist." % field_code, (field_code, ))


class EntityQuestionCodeNotSubmitted(MangroveException):
    def __init__(self):
        MangroveException.__init__(self, "The submission does not contain entity question code.")

class EntityTypeCodeNotSubmitted(MangroveException):
    def __init__(self):
        MangroveException.__init__(self, "The submission does not contain entity type code.")


class EntityQuestionAlreadyExistsException(MangroveException):
    pass


class QuestionCodeAlreadyExistsException(MangroveException):
    pass


class NumberNotRegisteredException(MangroveException):
    def __init__(self, from_number):
        MangroveException.__init__(self, ("Sorry, this number %s is not registered with us.") % (from_number,), (from_number,))


class MultipleReportersForANumberException(MangroveException):
    def __init__(self, from_number):
        MangroveException.__init__(self, ("Sorry, more than one reporter found for %s.") % (from_number,), (from_number,))


class EntityTypeDoesNotExistsException(MangroveException):
    def __init__(self, entity_type):
        MangroveException.__init__(self,
                                   ("Entity type %s doesnt exist.") % (".".join(entity_type),), (entity_type, ))


class InvalidAnswerSubmissionException(MangroveException):
    def __init__(self, message, data):
        MangroveException.__init__(self, message, data)



class AnswerTooBigException(InvalidAnswerSubmissionException):
    def __init__(self, code, answer):
        InvalidAnswerSubmissionException.__init__(self,
                                   ("Answer %s for question %s is greater than allowed.") % (answer, code,), (answer, code,))


class AnswerTooSmallException(InvalidAnswerSubmissionException):
    def __init__(self, code, answer):
        InvalidAnswerSubmissionException.__init__(self,
                                   ("Answer %s for question %s is smaller than allowed.") % (answer, code,), (answer, code,))


class AnswerTooLongException(InvalidAnswerSubmissionException):
    def __init__(self, code, answer):
        InvalidAnswerSubmissionException.__init__(self,
                                   ("Answer %s for question %s is longer than allowed.") % (answer, code,), (answer, code,))


class AnswerTooShortException(InvalidAnswerSubmissionException):
    def __init__(self, code, answer):
        InvalidAnswerSubmissionException.__init__(self,
                                   ("Answer %s for question %s is shorter than allowed.") % (answer, code,), (answer, code,))


class AnswerHasTooManyValuesException(InvalidAnswerSubmissionException):
    def __init__(self, code, answer):
        InvalidAnswerSubmissionException.__init__(self,
                                   ("Answer %s for question %s contains more than one value.") % (
                                   answer, code,), (answer, code,))


class AnswerHasNoValuesException(InvalidAnswerSubmissionException):
    def __init__(self, code, answer):
        InvalidAnswerSubmissionException.__init__(self,
                                   ("Answer %s for question %s has no value.") % (
                                   answer, code,), (answer, code,))


class AnswerNotInListException(InvalidAnswerSubmissionException):
    def __init__(self, code, answer):
        InvalidAnswerSubmissionException.__init__(self,
                                   ("Answer %s for question %s is not present in the allowed options.") % (
                                   answer, code,), (answer, code,))


class AnswerWrongType(InvalidAnswerSubmissionException):
    def __init__(self, code):
        InvalidAnswerSubmissionException.__init__(self, ("Answer to question %s is of wrong type.") % (code,), (code,))


class IncorrectDate(InvalidAnswerSubmissionException):
    def __init__(self, code, answer, date_format):
        InvalidAnswerSubmissionException.__init__(self, ('Answer to question %s is invalid: %s, expected date in %s format') %
                                         (code, answer, date_format), (code, answer, date_format))


class NoDocumentError(MangroveException):
    pass


class UnknownOrganization(MangroveException):
    def __init__(self, tel_number):
            MangroveException.__init__(self, ('No organization found for telephone number %s') %
                                             (tel_number,), (tel_number,))


class ShortCodeAlreadyInUseException(MangroveException):
    def __init__(self, short_code):
            MangroveException.__init__(self, ('The ID %s is already in use. Please specify another') %
                                             (short_code,), (short_code,))

class LatitudeNotFloat(InvalidAnswerSubmissionException):
    def __init__(self,lat):
        InvalidAnswerSubmissionException.__init__(self, ('The value for Latitude %s should be float') %
                                         (lat,), (lat,))

class LongitudeNotFloat(InvalidAnswerSubmissionException):
    def __init__(self,long):
        InvalidAnswerSubmissionException.__init__(self, ('The value for Longitude %s should be float') %
                                         (long,), (long,))
class LongitudeNotInRange(InvalidAnswerSubmissionException):
    def __init__(self,long):
        InvalidAnswerSubmissionException.__init__(self, ('%s is an invalid longitude, must be between -180 and 180') %
                                         (long,), (long,))
class LatitudeNotInRange(InvalidAnswerSubmissionException):
    def __init__(self,lat):
        MangroveException.__init__(self, ('%s is an invalid latitude, must be between -90 and 90') %
                                         (lat,), (lat,))

class GeoCodeFormatException(InvalidAnswerSubmissionException):
    def __init__(self, code):
        InvalidAnswerSubmissionException.__init__(self, "GPS coordinates must be in the format 'lat long'.", (code,))
