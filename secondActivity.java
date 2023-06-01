package com.example.todo;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class secondActivity extends AppCompatActivity {

    private TextView name,surname;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        name = findViewById(R.id.textName);
        surname = findViewById(R.id.textSurname);

        String username = getIntent().getStringExtra("keyname");
        String usersurname = getIntent().getStringExtra("keysurname");

        name.setText(username);
        surname.setText(usersurname);

    }
}
