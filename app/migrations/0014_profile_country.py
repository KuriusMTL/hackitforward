# Generated by Django 3.1 on 2020-09-30 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200919_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, choices=[('0', 'Afghanistan'), ('1', 'Albania'), ('2', 'Algeria'), ('3', 'American Samoa'), ('4', 'Andorra'), ('5', 'Angola'), ('6', 'Anguilla'), ('7', 'Antarctica'), ('8', 'Antigua and Barbuda'), ('9', 'Argentina'), ('10', 'Armenia'), ('11', 'Aruba'), ('12', 'Australia'), ('13', 'Austria'), ('14', 'Azerbaijan'), ('15', 'Bahamas'), ('16', 'Bahrain'), ('17', 'Bangladesh'), ('18', 'Barbados'), ('19', 'Belarus'), ('20', 'Belgium'), ('21', 'Belize'), ('22', 'Benin'), ('23', 'Bermuda'), ('24', 'Bhutan'), ('25', 'Bolivia, Plurinational State of'), ('26', 'Bolivia'), ('27', 'Bosnia and Herzegovina'), ('28', 'Botswana'), ('29', 'Bouvet Island'), ('30', 'Brazil'), ('31', 'British Indian Ocean Territory'), ('32', 'Brunei Darussalam'), ('33', 'Brunei'), ('34', 'Bulgaria'), ('35', 'Burkina Faso'), ('36', 'Burundi'), ('37', 'Cambodia'), ('38', 'Cameroon'), ('39', 'Canada'), ('40', 'Cape Verde'), ('41', 'Cayman Islands'), ('42', 'Central African Republic'), ('43', 'Chad'), ('44', 'Chile'), ('45', 'China'), ('46', 'Christmas Island'), ('47', 'Cocos (Keeling) Islands'), ('48', 'Colombia'), ('49', 'Comoros'), ('50', 'Congo'), ('51', 'Congo, the Democratic Republic of the'), ('52', 'Cook Islands'), ('53', 'Costa Rica'), ('54', "Côte d'Ivoire"), ('55', 'Ivory Coast'), ('56', 'Croatia'), ('57', 'Cuba'), ('58', 'Cyprus'), ('59', 'Czech Republic'), ('60', 'Denmark'), ('61', 'Djibouti'), ('62', 'Dominica'), ('63', 'Dominican Republic'), ('64', 'Ecuador'), ('65', 'Egypt'), ('66', 'El Salvador'), ('67', 'Equatorial Guinea'), ('68', 'Eritrea'), ('69', 'Estonia'), ('70', 'Ethiopia'), ('71', 'Falkland Islands (Malvinas)'), ('72', 'Faroe Islands'), ('73', 'Fiji'), ('74', 'Finland'), ('75', 'France'), ('76', 'French Guiana'), ('77', 'French Polynesia'), ('78', 'French Southern Territories'), ('79', 'Gabon'), ('80', 'Gambia'), ('81', 'Georgia'), ('82', 'Germany'), ('83', 'Ghana'), ('84', 'Gibraltar'), ('85', 'Greece'), ('86', 'Greenland'), ('87', 'Grenada'), ('88', 'Guadeloupe'), ('89', 'Guam'), ('90', 'Guatemala'), ('91', 'Guernsey'), ('92', 'Guinea'), ('93', 'Guinea-Bissau'), ('94', 'Guyana'), ('95', 'Haiti'), ('96', 'Heard Island and McDonald Islands'), ('97', 'Holy See (Vatican City State)'), ('98', 'Honduras'), ('99', 'Hong Kong'), ('100', 'Hungary'), ('101', 'Iceland'), ('102', 'India'), ('103', 'Indonesia'), ('104', 'Iran, Islamic Republic of'), ('105', 'Iraq'), ('106', 'Ireland'), ('107', 'Isle of Man'), ('108', 'Israel'), ('109', 'Italy'), ('110', 'Jamaica'), ('111', 'Japan'), ('112', 'Jersey'), ('113', 'Jordan'), ('114', 'Kazakhstan'), ('115', 'Kenya'), ('116', 'Kiribati'), ('117', "Korea, Democratic People's Republic of"), ('118', 'Korea, Republic of'), ('119', 'South Korea'), ('120', 'Kuwait'), ('121', 'Kyrgyzstan'), ('122', "Lao People's Democratic Republic"), ('123', 'Latvia'), ('124', 'Lebanon'), ('125', 'Lesotho'), ('126', 'Liberia'), ('127', 'Libyan Arab Jamahiriya'), ('128', 'Libya'), ('129', 'Liechtenstein'), ('130', 'Lithuania'), ('131', 'Luxembourg'), ('132', 'Macao'), ('133', 'Macedonia, the former Yugoslav Republic of'), ('134', 'Madagascar'), ('135', 'Malawi'), ('136', 'Malaysia'), ('137', 'Maldives'), ('138', 'Mali'), ('139', 'Malta'), ('140', 'Marshall Islands'), ('141', 'Martinique'), ('142', 'Mauritania'), ('143', 'Mauritius'), ('144', 'Mayotte'), ('145', 'Mexico'), ('146', 'Micronesia, Federated States of'), ('147', 'Moldova, Republic of'), ('148', 'Monaco'), ('149', 'Mongolia'), ('150', 'Montenegro'), ('151', 'Montserrat'), ('152', 'Morocco'), ('153', 'Mozambique'), ('154', 'Myanmar'), ('155', 'Burma'), ('156', 'Namibia'), ('157', 'Nauru'), ('158', 'Nepal'), ('159', 'Netherlands'), ('160', 'Netherlands Antilles'), ('161', 'New Caledonia'), ('162', 'New Zealand'), ('163', 'Nicaragua'), ('164', 'Niger'), ('165', 'Nigeria'), ('166', 'Niue'), ('167', 'Norfolk Island'), ('168', 'Northern Mariana Islands'), ('169', 'Norway'), ('170', 'Oman'), ('171', 'Pakistan'), ('172', 'Palau'), ('173', 'Palestinian Territory, Occupied'), ('174', 'Panama'), ('175', 'Papua New Guinea'), ('176', 'Paraguay'), ('177', 'Peru'), ('178', 'Philippines'), ('179', 'Pitcairn'), ('180', 'Poland'), ('181', 'Portugal'), ('182', 'Puerto Rico'), ('183', 'Qatar'), ('184', 'Réunion'), ('185', 'Romania'), ('186', 'Russian Federation'), ('187', 'Russia'), ('188', 'Rwanda'), ('189', 'Saint Helena, Ascension and Tristan da Cunha'), ('190', 'Saint Kitts and Nevis'), ('191', 'Saint Lucia'), ('192', 'Saint Pierre and Miquelon'), ('193', 'Saint Vincent and the Grenadines'), ('194', 'Saint Vincent & the Grenadines'), ('195', 'St. Vincent and the Grenadines'), ('196', 'Samoa'), ('197', 'San Marino'), ('198', 'Sao Tome and Principe'), ('199', 'Saudi Arabia'), ('200', 'Senegal'), ('201', 'Serbia'), ('202', 'Seychelles'), ('203', 'Sierra Leone'), ('204', 'Singapore'), ('205', 'Slovakia'), ('206', 'Slovenia'), ('207', 'Solomon Islands'), ('208', 'Somalia'), ('209', 'South Africa'), ('210', 'South Georgia and the South Sandwich Islands'), ('211', 'Spain'), ('212', 'Sri Lanka'), ('213', 'Sudan'), ('214', 'Suriname'), ('215', 'Svalbard and Jan Mayen'), ('216', 'Swaziland'), ('217', 'Sweden'), ('218', 'Switzerland'), ('219', 'Syrian Arab Republic'), ('220', 'Taiwan, Province of China'), ('221', 'Taiwan'), ('222', 'Tajikistan'), ('223', 'Tanzania, United Republic of'), ('224', 'Thailand'), ('225', 'Timor-Leste'), ('226', 'Togo'), ('227', 'Tokelau'), ('228', 'Tonga'), ('229', 'Trinidad and Tobago'), ('230', 'Trinidad & Tobago'), ('231', 'Tunisia'), ('232', 'Turkey'), ('233', 'Turkmenistan'), ('234', 'Turks and Caicos Islands'), ('235', 'Tuvalu'), ('236', 'Uganda'), ('237', 'Ukraine'), ('238', 'United Arab Emirates'), ('239', 'United Kingdom'), ('240', 'United States'), ('241', 'United States Minor Outlying Islands'), ('242', 'Uruguay'), ('243', 'Uzbekistan'), ('244', 'Vanuatu'), ('245', 'Venezuela, Bolivarian Republic of'), ('246', 'Venezuela'), ('247', 'Viet Nam'), ('248', 'Vietnam'), ('249', 'Virgin Islands, British'), ('250', 'Virgin Islands, U.S.'), ('251', 'Wallis and Futuna'), ('252', 'Western Sahara'), ('253', 'Yemen'), ('254', 'Zambia'), ('255', 'Zimbabwe')], max_length=3, null=True),
        ),
    ]
