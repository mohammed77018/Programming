package com.dracosoftrnd.waitingPatientSorter;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.TimePicker;

public class AddPatientActivity extends Activity {

	
	private Patient newPatient = null;
	
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_patient);
        
        bindControls();
    }

    private void bindControls() {
    	Button btnAdd = (Button)this.findViewById(R.id.btnAdd);
    	
    	Button btnCancel = (Button)this.findViewById(R.id.btnCancel);
    	btnCancel.setOnClickListener(new Button.OnClickListener() {
    	    public void onClick(View v) {
    	    	newPatient = null;
                AddPatientActivity.this.finish();
        }
    });
    	
    	TimePicker appointment = (TimePicker)this.findViewById(R.id.timeAppointment);
        appointment.setIs24HourView(true);
        
        TimePicker checkin = (TimePicker)this.findViewById(R.id.timeCheckin);
        checkin.setIs24HourView(true);
        
        CheckBox checkInNow = (CheckBox)this.findViewById(R.id.chkNow);
	}

	@Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.activity_add_patient, menu);
        return true;
    }
}
