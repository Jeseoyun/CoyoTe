# 취소되지 않은 진료 예약 조회하기
# https://school.programmers.co.kr/learn/courses/30/lessons/132204


WITH merged AS (
    SELECT apnt.apnt_no, pt.pt_name, pt.pt_no, dr.dr_name, apnt.apnt_ymd, apnt.apnt_cncl_yn, apnt.mcdp_cd
    FROM appointment AS apnt
    INNER JOIN doctor AS dr 
    ON apnt.mddr_id = dr.dr_id
    INNER JOIN patient AS pt
    ON apnt.pt_no = pt.pt_no
)

SELECT apnt_no, pt_name, pt_no, mcdp_cd, dr_name, apnt_ymd
FROM merged
WHERE apnt_ymd LIKE "2022-04-13%" AND apnt_cncl_yn='N' AND mcdp_cd="CS"
ORDER BY apnt_ymd ASC;