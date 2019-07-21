class Constants(object):
    @classmethod
    def get_constants(cls, template_file=None, action=None, context=None, model=None, paginate_by=None):
        return {
            'MODEL_NAME': model,
            'CONTEXT_OBJECT_NAME': context,
            'TEMPLATE_NAME': template_file + "/" + action + ".html",
            'PAGINATE_BY': paginate_by
        }
