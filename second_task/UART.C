#define FOSC 16000000UL
#define BAUD 9600
#define MYUBRR FOSC/16/BAUD-1 // this calculates the baud rate
#include <avr/io.h>



void USART_Init(unsigned int ubrr)
{
  /* 

  the UBRR is the baud rate setting and is splited into two parts the high bits and the lower one ,
  the way  "" >> 8 takes only the high byte ,
  the unsigned char make the register takes the low bytes only .

  */


  UBRR0H = (ubrr>>8); 
  UBRR0L = (unsigned char)ubrr;
  
  UCSR0B = (1<<RXEN0)|(1<<TXEN0);
  UCSR0C = (3<<UCSZ00);
  
}

unsigned char USART_RECEIVE()
{
  while (!(UCSR0A & (1<<RXC0))); // wait til there is data available to read
  
  	return UDR0;
}

void USART_TRANSMIT(unsigned char DATA)
{

  while (!(UCSR0A & (1<<UDRE0))); // wait till the  buffer is empty and ready to send new data 
    
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
  
  
  
  
  
  
  
  
  
  
  
  
  
  