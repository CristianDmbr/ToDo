package com.example.todo;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.ActionMode;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    private static final String LOG_TAG = "ActivityLifeCycle";

    private EditText name ,surname;
    private Button addButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        requestWindowFeature(Window.FEATURE_NO_TITLE);
        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        getSupportActionBar().hide();

        setContentView(R.layout.activity_main);

        Log.i(LOG_TAG,"Created");

        name = findViewById(R.id.nameView);
        surname = findViewById(R.id.surnameView);
        addButton = findViewById(R.id.button);

        addButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String userName = name.getText().toString();
                String userSurname = surname.getText().toString();

                Intent intent = new Intent(MainActivity.this,secondActivity.class);
                intent.putExtra("keyName",userName);
                intent.putExtra("keySurname",userSurname);

                startActivity(intent);

            }
        });

    }

    @Override
    protected void onStart() {
        super.onStart();
        Log.i(LOG_TAG,"Start");
    }

    @Override
    protected void onStop() {
        super.onStop();
        Log.i(LOG_TAG,"paused");
    }

    @Override
    protected void onResume() {
        super.onResume();
        Log.i(LOG_TAG,"Resumed");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.i(LOG_TAG,"Destroyed");
    }
}
