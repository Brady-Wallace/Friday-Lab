/*I am not the original author of this script,
this script has been used with permission from Anthony Romrell
Link to his Github: https://github.com/anthonyromrell
*/


using System.Globalization;
using TMPro;
using UnityEngine;
using UnityEngine.Events;
using System;

[RequireComponent(typeof(TextMeshProUGUI))]
public class TextMeshProBehaviour : MonoBehaviour
{
    private TextMeshProUGUI textObj;
    public UnityEvent awakeEvent, raiseEvent;
    private TimeSpan timeSpanObj;
    
    private void Start()
    {
        textObj = GetComponent<TextMeshProUGUI>();
        awakeEvent.Invoke();
    }

    private void Raise()
    {
        raiseEvent.Invoke();
    }
    

    public void UpdateText(string obj)
    {
        textObj.text = obj;
    }

    public void UpdateText(FloatData obj)
    {
        textObj.text = obj.Value.ToString(CultureInfo.CurrentCulture);
    }

    public void UpdateTextWithTime(FloatData obj)
    {
        timeSpanObj = TimeSpan.FromSeconds(obj.Value);
        if (timeSpanObj.Seconds > 9)
        {

            textObj.text = timeSpanObj.Minutes + ":" + timeSpanObj.Seconds;
        }

        else
        {
            textObj.text = timeSpanObj.Minutes + ":" + "0" + timeSpanObj.Seconds;
        }
    }
}