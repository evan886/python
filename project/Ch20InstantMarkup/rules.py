class Rule:
    """
    Base class for all rules.
    """
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True 


class HeadingRule:
    """
    A heading is a single line that is at most 70 characters and
    that doesn't end with a colon.
    """
    type = 'heading'
    def codition(self,block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

class TitleRule(HeadingRule):
    """
    The title is the first block in the document, provided that
    it is a heading.
    """
    type = 'title'
    first = True  

    def condition(self,block):
        if not self.first: return False 
        self.first = False
        return HeadingRule.condition(self,block)

class ListItemRule(Rule):

    type = 'listitem'
    def condition(self,block):
        return block[0] == '-'
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True 

class ListRule(ListItemRule):


    type = 'list'
    inside = False
    def condiiton(self,block):
        return True
    def action(self,block,handler):
        