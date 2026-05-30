<link rel='stylesheet' type='text/css' href='/main.css' />
%from datetime import datetime
<h1>Notes</h1>
<table>
  <tr>
    <th>Date</th>
    <th>Note</th>
  </tr>
  %for document in cursor:
  %  date = datetime.strftime(document['date'], '%m/%d/%Y %H:%M:%S')
    <tr>
      <td>{{date}}</td>
      <td>{{document['note']}}</td>
    </tr>
  %end
</table>

