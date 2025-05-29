SELECT a.apnt_no, p.pt_name, p.pt_no, a.mcdp_cd, d.dr_name, a.apnt_ymd
FROM appointment AS a
    JOIN patient as p ON a.pt_no = p.pt_no
    JOIN doctor as d ON a.mddr_id = d.dr_id
WHERE (a.apnt_ymd >= '2022-04-13 00:00:00.000000' AND a.apnt_ymd < '2022-04-14 00:00:00.000000')
    AND (a.mcdp_cd = 'CS')
    AND a.apnt_cncl_yn = 'N'
ORDER BY a.apnt_ymd;