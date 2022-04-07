from sly import Lexer

class BasicLexer(Lexer):
  # Set of token names. This is always required 
  tokens = {  PLUS, MINUS, TIMES,
              ASSIGN, LPAREN, RPAREN, SCOLON,
              LBRACK, RBRACK, AND, LESS,
              COLON, DOT, NOT, LBRACE, RBRACE,
              IF, ELSE, WHILE, CLASS, PUBLIC, STATIC, VOID, MAIN, STRING, EXTENDS, INT, BOOLEAN, SYSTEM, OUT, PRINTLN, RETURN, THIS, LENGTH, NEW, TRUE,FALSE, ID, NUM, KEYWORD}
  
  
  # String containing ignored characters between tokens
  ignore = ' \t'
  
  #Átomos que representam palavras reservdadas da linguagem
  
  ID['class'] = KEYWORD
  ID['String'] = KEYWORD
  ID['public'] = KEYWORD
  ID['static'] = KEYWORD
  ID['void'] = KEYWORD
  ID['main'] = KEYWORD
  ID['extends'] = KEYWORD
  ID['return'] = KEYWORD
  ID['boolean'] = KEYWORD
  ID['int'] = KEYWORD
  ID['if'] = KEYWORD
  ID['else'] = KEYWORD
  ID['while'] = KEYWORD
  ID['System'] = KEYWORD
  ID['out'] = KEYWORD
  ID['println'] = KEYWORD
  ID['true'] = KEYWORD
  ID['false'] = KEYWORD
  ID['this'] = KEYWORD
  ID['new'] = KEYWORD
  ID['length'] = KEYWORD
  
  #  Átomos que representam símbolos da linguagem
  
  PLUS    = r'\+'
  MINUS   = r'\-'
  ASSIGN  = r'='
  LPAREN  = r'\('
  RPAREN  = r'\)'
  SCOLON  = r';'
  LBRACK = r'\['
  RBRACK = r'\]'
  AND = r'&&'
  LESS = r'\<'
  COLON = r','
  DOT = r'\.'
  NOT = r'!'
  LBRACE = '{'
  RBRACE = '}'
  
  
  #Átomos com regras de formação complexa
  
  @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
  def ID(self, t):
    return t

  @_(r'\d+')
  def NUM(self, t):
    t.value = int(t.value) 
    return t
  @_(r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)|(\/[\*]*[\r\n])')
  def COMMENT(self, t):
    x = t.value.count("\n")
    if x == 0:
      pass
    else:    
      self.lineno = self.lineno + x
      pass
      
  @_(r'\*')
  def TIMES(self, t):
    return t

  @_(r'\n+')
  def ignore_newline(self, t):
    self.lineno += len(t.value)
  
  def error(self, t):
    print('Linha: %d - Caractere ilegal: "%s"' % (self.lineno, t.value[0]))
    self.index += 1   


def vailexer(data):
  lexer = BasicLexer()
  for tok in lexer.tokenize(data):
    print('[ %d, %s, "%s" ]' % (tok.lineno,tok.type,tok.value))