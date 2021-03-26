package com.calculadora.br;

import android.support.v7.app.AppCompatActivity;
import android.app.Activity;
import android.os.Bundle;

import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private EditText val1,val2;
    private Button btSom, btSub, btMult, btDiv;

    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        val1 = (EditText) findViewById(R.id.edtVal1);
        val2 = (EditText) findViewById(R.id.edtVal2);

        btSom = (Button) findViewById(R.id.btSom);
        btSub = (Button) findViewById(R.id.btSub);
        btMult = (Button) findViewById(R.id.btMult);
        btDiv = (Button) findViewById(R.id.btDiv);
        
        
        //Soma
        btSom.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
            	if(!vazio()){
            		double result = Double.parseDouble(val1.getText().toString()) + Double.parseDouble(val2.getText().toString());
            		Toast.makeText(MainActivity.this, "Resultado: " + result, Toast.LENGTH_SHORT).show();
            	}
            }
        });

        //Subtrao
        btSub.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
            	if(!vazio()){
            		double result = Double.parseDouble(val1.getText().toString()) - Double.parseDouble(val2.getText().toString());
            		Toast.makeText(MainActivity.this, "Resultado: " + result, Toast.LENGTH_SHORT).show();
            	}
            }
        });

        //Multiplicao
        btMult.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
            	if(!vazio()){
            		double result = Double.parseDouble(val1.getText().toString()) * Double.parseDouble(val2.getText().toString());
            		Toast.makeText(MainActivity.this, "Resultado: " + result, Toast.LENGTH_SHORT).show();
            	}
            }
        });
        
        
         //Diviso
        btDiv.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(val2.getText().toString() == "0"){
                    Toast.makeText(MainActivity.this, "Impossível dividir por zero!", Toast.LENGTH_SHORT).show();

                }else if(!vazio()){
                    double result = Double.parseDouble(val1.getText().toString()) / Double.parseDouble(val2.getText().toString());
                    Toast.makeText(MainActivity.this, "Resultado: " + result, Toast.LENGTH_SHORT).show();
                }
            }
        });
        
        
       
    }
    
    private boolean vazio(){
    	if(val1.getText().toString().length() == 0 && val2.getText().toString().length() == 0){
    		return true;
    	}else{
    		return false;
    	}
    }
}
