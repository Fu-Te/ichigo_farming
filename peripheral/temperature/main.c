

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include "nrf.h"
#include "nrf_delay.h"
#include "app_error.h"
#include "bsp.h"

#include "nrf_log.h"
#include "nrf_log_ctrl.h"
#include "nrf_log_default_backends.h"


#define DHT11_PIN 7

int DHT11ReadByte(void)
{
  int ByteData=0,i;
  unsigned long int counter=0;
  for(i=0;i<8;i++)
  {
    ByteData = ByteData * 2;
    counter = 0;
    while(0==(nrf_gpio_pin_read(DHT11_PIN))) // may be 50us
    {
      counter++;
      nrf_delay_us(1);
      if ( 200 < counter  ){
        NRF_LOG_INFO("error1\n");
        return -1;
      }
    }
    counter = 0;
    while(1==(nrf_gpio_pin_read(DHT11_PIN)))
    {
      counter++;
      nrf_delay_us(1);
      if ( 200 < counter  ){
        NRF_LOG_INFO("error2\n");
        return -1;
      }
    }
    if(counter<30)  // 40... error
    {
            // 26-28us : Bit data "0"
    } else {
      ByteData = ByteData +1; // 70us : Bit data "1"
    }           
  }
  return ByteData;
}

void DHT11ReadData()
{   
  int counter,err,humiInt,humiDec,tempInt,tempDec,checkSum,decimal_value1,decimal_value2,decimal_value3;
  nrf_gpio_pin_set(DHT11_PIN);
  nrf_delay_ms(250);
  nrf_gpio_cfg_output(DHT11_PIN);
  nrf_gpio_pin_clear(DHT11_PIN);   // Send Start Signal
  nrf_delay_ms(20);   
  nrf_gpio_pin_set(DHT11_PIN);
  nrf_delay_us(40);                // Send Start Signal end
  nrf_gpio_cfg_input(DHT11_PIN, NRF_GPIO_PIN_PULLUP);
  nrf_delay_us(1);
  counter=0;
  while(nrf_gpio_pin_read(DHT11_PIN)==0) // Receive LOW answer ( 83us)
  {
    nrf_delay_us(1);
    counter++;
    if ( 200 < counter ){
        NRF_LOG_INFO("got wrong start1\n");
        return;
    }
  }
  counter=0;
  while(nrf_gpio_pin_read(DHT11_PIN)==1) // Recieve High answer ( 87us)
  {
    nrf_delay_us(1);
    counter++;
    if ( 200 < counter ){
      NRF_LOG_INFO("got wrong start2\n");
      return;
    }
  }
  humiInt = DHT11ReadByte();
  humiDec = DHT11ReadByte();
  tempInt = DHT11ReadByte();
  tempDec = DHT11ReadByte();
  checkSum = DHT11ReadByte();

  if (((humiInt + humiDec + tempInt + tempDec) & 0xff) != checkSum) 
  {
     NRF_LOG_INFO("got wrong values\n");
     return -1;
  } else {
    if ( 127 < tempDec ){
      tempInt=0-tempInt;
      tempDec=tempDec-128;
    }
    NRF_LOG_INFO("TEMP: %d.%d  HUMI: %d.%d",tempInt,tempDec,humiInt,humiDec);
  }
}


int main(void)
{
    APP_ERROR_CHECK(NRF_LOG_INIT(NULL));
    NRF_LOG_DEFAULT_BACKENDS_INIT();
    NRF_LOG_INFO("Temp/Humi sensor DHT11 example started.");
    nrf_gpio_cfg_input(DHT11_PIN, NRF_GPIO_PIN_PULLUP);
    SEGGER_RTT_WriteString(0, "DHT11 init complete\n");
    while (true)
    {
        DHT11ReadData();
        nrf_delay_ms(3000);
        NRF_LOG_FLUSH();
    }
}

