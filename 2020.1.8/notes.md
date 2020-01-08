# 2020.1.8 Study Notes

1. Learning basic JAVA
2. Learning how to write an android app.

## Summary of An Android App

```java
public class MainActivity extends AppCompatActivity {
    private int mCount = 0;
    private TextView mShowCount;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mShowCount = (TextView) findViewById(R.id.show_count);
    }
    
    public void showToast(View view) {
        Toast toast = Toast.makeText(this, R.string.toast_message, Toast.LENGTH_SHORT);
        toast.show();
    }
    
    public void countUp(View view) {
        mCount++;
        if (mShowCount != null) {
            mShowCount.setText(Integer.toString(mCount));
        }
    }
}
```

### Some Important Ideas

- Extracting string resources
- Handling clicks: `android:onClick`
- Toast
  - Call the `makeText()` factory method
  - Context is needed
- XML file