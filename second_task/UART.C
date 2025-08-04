#define FOSC 16000000UL
#define BAUD 9600
#define MYUBRR FOSC/16/BAUD-1
#include <avr/io.h>



void USART_Init(unsigned int ubrr)
{
  
  UBRR0H = (unsigned char)(ubrr>>8);
  UBRR0L = (unsigned char)ubrr;
  
  UCSR0B = (1<<RXEN0)|(1<<TXEN0);
  UCSR0C = (3<<UCSZ00);
  
}

unsigned char USART_RECEIVE()
{
  while (!(UCSR0A & (1<<RXC0)));
  
  	return UDR0;
}

void USART_TRANSMIT(unsigned char DATA)
{

  while (!(UCSR0A & (1<<UDRE0)));
    
  UDR0 = DATA + 1 ;
  
}
  
  int main ()
  {
    
    USART_Init(MYUBRR);
    
    while (1)
      
    {   
      USART_TRANSMIT(USART_RECEIVE());
    }
    
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  