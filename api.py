XML_TEMPLATE = """
<time_entry>
    <issue_id>{issue}</issue_id>
    <activity_id>{activity}</activity_id>
    <hours>{duration}</hours>
    <comments>{comment}</comments>
    <spent_on>{date}</spent_on>
    <custom_fields type="array">
        <custom_field id="1">
            <value>{start}</value>
        </custom_field>
        <custom_field id="2">
            <value>{end}</value>
        </custom_field>
        <custom_field id="3">
            <value>شرکت</value>
        </custom_field>
        <custom_field id="6">
            <value>0</value>
        </custom_field>
    </custom_fields>
</time_entry>
"""